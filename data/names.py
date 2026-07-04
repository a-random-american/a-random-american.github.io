

import os
import pandas as pd
from collections import defaultdict

DATA_DIR = "/Users/joshuatint/Downloads/namesbystate"
OUTPUT_TS = "names.ts"

TOP_N = 500

FALLBACKS = {
    "PR": "FL",
    "GU": "HI",
    "AS": "HI",
    "MP": "HI",
    "VI": "FL"
}

STATE_ABBR_TO_NAME = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas",
    "CA": "California", "CO": "Colorado", "CT": "Connecticut",
    "DE": "Delaware", "DC": "District of Columbia", "FL": "Florida",
    "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois",
    "IN": "Indiana", "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky",
    "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
    "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota",
    "MS": "Mississippi", "MO": "Missouri", "MT": "Montana",
    "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire",
    "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
    "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio",
    "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania",
    "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota",
    "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont",
    "VA": "Virginia", "WA": "Washington", "WV": "West Virginia",
    "WI": "Wisconsin", "WY": "Wyoming", "AS": "American Samoa", "GU": "Guam", "MP": "Northern Mariana Islands", "PR": "Puerto Rico", "VI": "U.S. Virgin Islands"
}

def decade(year):
    return (year // 10) * 10

def load_state_file(path):
    return pd.read_csv(
        path,
        header=None,
        names=["state", "sex", "year", "name", "count"]
    )

def build_distributions():
    agg = defaultdict(lambda: defaultdict(int))
    totals = defaultdict(int)

    for file in os.listdir(DATA_DIR):
        if not file.endswith(".TXT"):
            continue

        abbr = file.replace(".TXT", "")
        df = load_state_file(os.path.join(DATA_DIR, file))

        for _, row in df.iterrows():
            dec = decade(row["year"])
            key = (abbr, row["sex"], dec)
            name = row["name"]

            agg[key][name] += row["count"]
            totals[key] += row["count"]

    # Normalize
    probs = {}
    for key, names in agg.items():
        total = totals[key]

        # keep top N
        sorted_names = sorted(names.items(), key=lambda x: -x[1])[:TOP_N]

        probs[key] = {
            name: count / total
            for name, count in sorted_names
        }

    return probs

def apply_fallbacks(probs):
    final = {}

    for abbr in list(STATE_ABBR_TO_NAME.keys()) + list(FALLBACKS.keys()):
        source = abbr if abbr in STATE_ABBR_TO_NAME else FALLBACKS.get(abbr)

        for gender in ["M", "F"]:
            for dec in range(1910, 2020, 10):
                key = (abbr, gender, dec)
                src_key = (source, gender, dec)

                if src_key in probs:
                    final[key] = probs[src_key]

    return final

def export_ts(probs):
    state_maps = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))

    for (abbr, gender, dec), names in probs.items():
        state = STATE_ABBR_TO_NAME.get(abbr, abbr)

        for name, prob in names.items():
            state_maps[state][gender][dec][name] = round(prob, 8)

    with open(OUTPUT_TS, "w") as f:
        f.write("export const names = {\n")

        for state, genders in state_maps.items():
            f.write(f'  "{state}": new Map([\n')

            for gender, decades in genders.items():
                f.write(f'    ["{gender}", new Map([\n')

                for dec, name_map in decades.items():
                    f.write(f'      [{dec}, new Map([\n')

                    for name, prob in name_map.items():
                        f.write(f'        ["{name}", {prob}],\n')

                    f.write("      ])],\n")

                f.write("    ])],\n")

            f.write("  ]),\n")

        f.write("};\n")

if __name__ == "__main__":
    print("Building distributions...")
    probs = build_distributions()

    print("Applying fallbacks...")
    probs = apply_fallbacks(probs)

    print("Exporting TS...")
    export_ts(probs)

    print("Done!")