import pandas as pd
from collections import defaultdict

INPUT_FILE = "../src/namesbyrace.csv"
OUTPUT_TS = "names_by_race.ts"

RACE_COLUMNS = {
    "White": 5,
    "Black": 6,
    "Native American": 7,
    "Asian": 8,
    "Multiracial": 9,
    "Hispanic": 10,
}

def main():
    df = pd.read_csv(INPUT_FILE, sep=",", header=None)

    df.columns = [
        "name", "rank", "count", "prop100k", "cumprop",
        "white", "black", "native", "asian_pi", "multi", "hispanic"
    ]

    # Normalize names
    df["name"] = df["name"].str.title()

    race_maps = defaultdict(dict)

    # Build raw weights
    for _, row in df.iterrows():
        name = row["name"]

        race_maps["White"][name] = row["white"]
        race_maps["Black"][name] = row["black"]
        race_maps["Native American"][name] = row["native"]
        race_maps["Asian"][name] = row["asian_pi"]
        race_maps["Multiracial"][name] = row["multi"]
        race_maps["Hispanic"][name] = row["hispanic"]

    # Normalize per race
    for race, names in race_maps.items():
        total = sum(names.values())
        if total == 0:
            continue

        for name in names:
            names[name] /= total

    # Export TS
    with open(OUTPUT_TS, "w") as f:
        f.write("export const namesByRace: Record<string, Map<string, number>> = {\n")

        for race, names in race_maps.items():
            f.write(f'  "{race}": new Map([\n')

            for name, prob in sorted(names.items(), key=lambda x: -x[1])[:1000]:
                f.write(f'    ["{name}", {round(prob, 8)}],\n')

            f.write("  ]),\n")

        f.write("};\n")

    print("Done!")

if __name__ == "__main__":
    main()