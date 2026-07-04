import pandas as pd
from collections import defaultdict

INPUT_FILES = [
    "/Users/joshuatint/Downloads/csv_pus/psam_pusa.csv",
    "/Users/joshuatint/Downloads/csv_pus/psam_pusb.csv",
    "/Users/joshuatint/Downloads/csv_pus/psam_pusc.csv",
    "/Users/joshuatint/Downloads/csv_pus/psam_pusd.csv",
    "/Users/joshuatint/Downloads/csv_pus/psam_p72.csv"
]
OUTPUT_TS = "demographics.ts"
CHUNK_SIZE = 100_000

STATE_MAP = {
    1: "Alabama", 2: "Alaska", 4: "Arizona", 5: "Arkansas", 6: "California",
    8: "Colorado", 9: "Connecticut", 10: "Delaware", 11: "District of Columbia",
    12: "Florida", 13: "Georgia", 15: "Hawaii", 16: "Idaho", 17: "Illinois",
    18: "Indiana", 19: "Iowa", 20: "Kansas", 21: "Kentucky", 22: "Louisiana",
    23: "Maine", 24: "Maryland", 25: "Massachusetts", 26: "Michigan",
    27: "Minnesota", 28: "Mississippi", 29: "Missouri", 30: "Montana",
    31: "Nebraska", 32: "Nevada", 33: "New Hampshire", 34: "New Jersey",
    35: "New Mexico", 36: "New York", 37: "North Carolina",
    38: "North Dakota", 39: "Ohio", 40: "Oklahoma", 41: "Oregon",
    42: "Pennsylvania", 44: "Rhode Island", 45: "South Carolina",
    46: "South Dakota", 47: "Tennessee", 48: "Texas", 49: "Utah",
    50: "Vermont", 51: "Virginia", 53: "Washington", 54: "West Virginia",
    55: "Wisconsin", 56: "Wyoming", 60: "American Samoa", 66: "Guam",
    69: "Northern Mariana Islands", 72: "Puerto Rico", 78: "U.S. Virgin Islands"
}

def age_bucket(age):
    return (age // 10) * 10

def map_gender(sex):
    return "Male" if sex == 1 else "Female"

def map_race(rac1p, hisp):
    # FIXED: correct Hispanic logic
    if hisp != 1:
        return "Hispanic"
    if rac1p == 1:
        return "White"
    elif rac1p == 2:
        return "Black"
    elif rac1p in [3, 4, 5]:
        return "Native American"
    elif rac1p == 6:
        return "Asian"
    elif rac1p == 7:
        return "Pacific Islander"
    elif rac1p == 9:
        return "Multiracial"
    return "Some Other Race"

def nb_rate(age):
    if age < 18:
        return 0.0
    elif age < 30:
        return 0.05
    elif age < 50:
        return 0.02
    else:
        return 0.005

if __name__ == "__main__":
    agg = defaultdict(float)

    print("Streaming + aggregating...")

    usecols = ["STATE", "AGEP", "SEX", "RAC1P", "HISP", "PWGTP"]

    dtypes = {
        "STATE": "int16",
        "AGEP": "int16",
        "SEX": "int8",
        "RAC1P": "int8",
        "HISP": "int8",
        "PWGTP": "float32"
    }

    for file in INPUT_FILES:
        print(f"Processing {file}...")

        for chunk in pd.read_csv(file, usecols=usecols, dtype=dtypes, chunksize=CHUNK_SIZE):

            chunk = chunk[chunk["STATE"].isin(STATE_MAP)]

            # vectorized transformations
            chunk["age_bucket"] = (chunk["AGEP"] // 10) * 10
            chunk["gender"] = chunk["SEX"].map({1: "Male", 2: "Female"})

            # race mapping (vectorized via apply once)
            chunk["race"] = chunk.apply(
                lambda r: map_race(r["RAC1P"], r["HISP"]), axis=1
            )

            chunk["state_name"] = chunk["STATE"].map(STATE_MAP)

            grouped = (
                chunk.groupby(["state_name", "age_bucket", "gender", "race"])["PWGTP"]
                .sum()
            )

            for key, val in grouped.items():
                agg[key] += val

    # -----------------------------
    # NORMALIZE
    # -----------------------------
    state_totals = defaultdict(float)
    for (state, age, gender, race), val in agg.items():
        state_totals[state] += val

    grouped = defaultdict(dict)

    for (state, age, gender, race), val in agg.items():
        grouped[(state, age, race)][gender] = val / state_totals[state]

    # debug check
    gender_totals = defaultdict(float)
    for (_, _, _), genders in grouped.items():
        for g, v in genders.items():
            gender_totals[g] += v
    print("Gender totals:", gender_totals)

    # -----------------------------
    # ADD NB
    # -----------------------------
    final = {}

    for (state, age, race), genders in grouped.items():
        male = genders.get("Male", 0.0)
        female = genders.get("Female", 0.0)
        total = male + female

        if total == 0:
            continue

        nb_p = nb_rate(age)

        final[(state, age, "Male", race)] = male * (1 - nb_p)
        final[(state, age, "Female", race)] = female * (1 - nb_p)
        final[(state, age, "Nonbinary", race)] = total * nb_p

    # renormalize
    norm = defaultdict(float)
    for (state, age, gender, race), val in final.items():
        norm[state] += val

    for key in final:
        state = key[0]
        final[key] /= norm[state]

    # -----------------------------
    # EXPORT TS
    # -----------------------------
    state_maps = defaultdict(list)

    for (state, age, gender, race), prob in final.items():
        state_maps[state].append(([age, gender, race], round(prob, 8)))

    with open(OUTPUT_TS, "w") as f:
        f.write("export const demographics: Record<State, Map<[Age, Gender, Race], number>> = {\n")
        for state, entries in state_maps.items():
            f.write(f'  "{state}": new Map([\n')
            for key, val in entries:
                f.write(f'    [[{key[0]}, "{key[1]}", "{key[2]}"], {val}],\n')
            f.write("  ]),\n")
        f.write("};\n")

    print("Done!")