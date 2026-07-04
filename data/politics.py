import json
from collections import defaultdict

if __name__ == "__main__":
    OUTPUT_FILE = "../src/politics.ts"

    POLITICS = ["Democrat", "Republican", "Independent"]

    # -----------------------------
    # LOAD DATA
    # -----------------------------
    with open("../src/race_by_state.json") as f:
        P_race_given_state = json.load(f)

    with open("pew_politics.json") as f:
        P_politics_given_rag = json.load(f)
        # keyed as: race -> gender -> age_bucket -> {D, R, I}

    # -----------------------------
    # NORMALIZATION HELPERS
    # -----------------------------
    def normalize(dist):
        total = sum(dist.values())
        if total == 0:
            return dist
        return {k: v / total for k, v in dist.items()}

    # -----------------------------
    # MODEL
    # -----------------------------
    def compute_state_distribution(state):
        race_dist = P_race_given_state[state]

        result = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
        # age -> gender -> politics

        for race, p_race in race_dist.items():
            if race not in P_politics_given_rag:
                continue

            for gender in P_politics_given_rag[race]:
                for age_bucket in P_politics_given_rag[race][gender]:

                    politics_dist = P_politics_given_rag[race][gender][age_bucket]

                    for pol in POLITICS:
                        result[age_bucket][gender][pol] += (
                                p_race * politics_dist.get(pol, 0)
                        )

        # normalize per (age, gender)
        for age in result:
            for gender in result[age]:
                result[age][gender] = normalize(result[age][gender])

        return result

    # -----------------------------
    # RUN ALL STATES
    # -----------------------------
    final = {}

    for state in P_race_given_state:
        final[state] = compute_state_distribution(state)

    # -----------------------------
    # EXPORT TYPESCRIPT
    # -----------------------------
    with open(OUTPUT_FILE, "w") as f:
        f.write("export const politics = {\n")

        for state, age_map in final.items():
            f.write(f'  "{state}": {{\n')

            for age, gender_map in age_map.items():
                f.write(f'    {age}: {{\n')

                for gender, dist in gender_map.items():
                    f.write(f'      "{gender}": {{')

                    f.write(
                        ", ".join(
                            f'"{k}": {v:.6f}' for k, v in dist.items()
                        )
                    )

                    f.write("},\n")

                f.write("    },\n")

            f.write("  },\n")

        f.write("};\n")

    print("Done.")

