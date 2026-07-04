ITERATIONS = 15  # usually converges fast

final = {}

from collections import defaultdict

OUTPUT_TS = "territories.ts"

# -----------------------------
# INPUT DATA (you provided)
# -----------------------------

RACE_TOTALS = {
    "American Samoa": {"White": 374, "Black": 24, "Native American": 13, "Asian": 2878, "Pacific Islander": 44090, "Some Other Race": 139, "Multiracial": 2192, "Hispanic": 44090},
    "Guam": {"White": 10491, "Black": 1340, "Native American": 214, "Asian": 54586, "Pacific Islander": 70809, "Some Other Race": 955, "Multiracial": 15441, "Hispanic": 70809},
    "Northern Mariana Islands": {"White": 1015, "Black": 65, "Native American": 12, "Asian": 22054, "Pacific Islander": 20665, "Some Other Race": 65, "Multiracial": 3453, "Hispanic": 20665},
    "U.S. Virgin Islands": {"White": 11036, "Black": 55936, "Native American": 371, "Asian": 910, "Pacific Islander": 51, "Some Other Race": 1750, "Multiracial": 2349, "Hispanic": 51},
}

# age buckets → (male, female)
AGE_SEX = {
    "Guam": {
        0:(8032,7525),10:(7663,7088),20:(7342,6165),30:(5787,5376),
        40:(4412,4372),50:(5245,4767),60:(4121,3981),70:(2354,2558),
        80:(717,1027),90:(85,165)
    },
    "Northern Mariana Islands": {
        0:(2495,2357),10:(1971,1529),20:(1607,1791),30:(1008,2688),
        40:(1858,1726),50:(1824,1617),60:(769,671),70:(248,168),
        80:(54,93),90:(4,12)
    },
    "American Samoa": {
        0:(3417,3194),10:(3214,3065),20:(1944,1947),30:(1726,1784),
        40:(1793,1807),50:(1335,1344),60:(755,725),70:(321,333),
        80:(76,130),90:(41,69)
    },
    "U.S. Virgin Islands": {
        0:(3736,3764),10:(3849,3635),20:(2707,3187),30:(2825,3312),
        40:(3506,3944),50:(3800,4100),60:(3510,3857),70:(1739,1978),
        80:(568,764),90:(380,774)
    }
}

# -----------------------------
# HAWAII DISTRIBUTION (PASTE YOUR MAP HERE)
# -----------------------------

hawaii_data = [
    # paste your Hawaii entries as tuples:
    # (age, gender, race, prob)
    [0, "Male", "Asian", 0.01161956],
    [0, "Female", "Asian", 0.01084045],
    [0, "Nonbinary", "Asian", 0.0],
    [0, "Male", "Black", 0.00094033],
    [0, "Female", "Black", 0.00084554],
    [0, "Nonbinary", "Black", 0.0],
    [0, "Male", "Hispanic", 0.01144589],
    [0, "Female", "Hispanic", 0.01071521],
    [0, "Nonbinary", "Hispanic", 0.0],
    [0, "Male", "Multiracial", 0.01939961],
    [0, "Female", "Multiracial", 0.01870838],
    [0, "Nonbinary", "Multiracial", 0.0],
    [0, "Male", "Native American", 1.38e-06],
    [0, "Female", "Native American", 5.674e-05],
    [0, "Nonbinary", "Native American", 0.0],
    [0, "Male", "Pacific Islander", 0.00647853],
    [0, "Female", "Pacific Islander", 0.00574716],
    [0, "Nonbinary", "Pacific Islander", 0.0],
    [0, "Male", "Some Other Race", 0.00040409],
    [0, "Female", "Some Other Race", 0.0002401],
    [0, "Nonbinary", "Some Other Race", 0.0],
    [0, "Male", "White", 0.00812325],
    [0, "Female", "White", 0.0078361],
    [0, "Nonbinary", "White", 0.0],
    [10, "Male", "Asian", 0.01571786],
    [10, "Female", "Asian", 0.01401848],
    [10, "Nonbinary", "Asian", 0.0],
    [10, "Male", "Black", 0.00085868],
    [10, "Female", "Black", 0.00070715],
    [10, "Nonbinary", "Black", 0.0],
    [10, "Male", "Hispanic", 0.00903244],
    [10, "Female", "Hispanic", 0.00844223],
    [10, "Nonbinary", "Hispanic", 0.0],
    [10, "Male", "Multiracial", 0.01838594],
    [10, "Female", "Multiracial", 0.01782755],
    [10, "Nonbinary", "Multiracial", 0.0],
    [10, "Male", "Native American", 1.591e-05],
    [10, "Female", "Native American", 4.636e-05],
    [10, "Nonbinary", "Native American", 0.0],
    [10, "Male", "Pacific Islander", 0.00711718],
    [10, "Female", "Pacific Islander", 0.0070473],
    [10, "Nonbinary", "Pacific Islander", 0.0],
    [10, "Male", "Some Other Race", 0.00026293],
    [10, "Female", "Some Other Race", 0.00014876],
    [10, "Nonbinary", "Some Other Race", 0.0],
    [10, "Male", "White", 0.00726595],
    [10, "Female", "White", 0.00704453],
    [10, "Nonbinary", "White", 0.0],
    [20, "Male", "Asian", 0.01774864],
    [20, "Female", "Asian", 0.01565963],
    [20, "Nonbinary", "Asian", 0.00175833],
    [20, "Male", "Black", 0.00279826],
    [20, "Female", "Black", 0.00118714],
    [20, "Nonbinary", "Black", 0.00020976],
    [20, "Male", "Hispanic", 0.00835667],
    [20, "Female", "Hispanic", 0.00738119],
    [20, "Nonbinary", "Hispanic", 0.00082831],
    [20, "Male", "Multiracial", 0.01213436],
    [20, "Female", "Multiracial", 0.01344902],
    [20, "Nonbinary", "Multiracial", 0.00134649],
    [20, "Male", "Native American", 0.00013541],
    [20, "Female", "Native American", 3.944e-05],
    [20, "Nonbinary", "Native American", 9.2e-06],
    [20, "Male", "Pacific Islander", 0.00611188],
    [20, "Female", "Pacific Islander", 0.00563334],
    [20, "Nonbinary", "Pacific Islander", 0.00061817],
    [20, "Male", "Some Other Race", 0.00020049],
    [20, "Female", "Some Other Race", 0.0001387],
    [20, "Nonbinary", "Some Other Race", 1.785e-05],
    [20, "Male", "White", 0.01561033],
    [20, "Female", "White", 0.01058897],
    [20, "Nonbinary", "White", 0.00137891],
    [30, "Male", "Asian", 0.01955409],
    [30, "Female", "Asian", 0.02176399],
    [30, "Nonbinary", "Asian", 0.00084323],
    [30, "Male", "Black", 0.00235365],
    [30, "Female", "Black", 0.00119276],
    [30, "Nonbinary", "Black", 7.238e-05],
    [30, "Male", "Hispanic", 0.00752545],
    [30, "Female", "Hispanic", 0.00721963],
    [30, "Nonbinary", "Hispanic", 0.00030092],
    [30, "Male", "Multiracial", 0.01613041],
    [30, "Female", "Multiracial", 0.01446706],
    [30, "Nonbinary", "Multiracial", 0.00062444],
    [30, "Male", "Native American", 4.95e-05],
    [30, "Female", "Native American", 0.00010646],
    [30, "Nonbinary", "Native American", 3.18e-06],
    [30, "Male", "Pacific Islander", 0.00686702],
    [30, "Female", "Pacific Islander", 0.00595024],
    [30, "Nonbinary", "Pacific Islander", 0.00026158],
    [30, "Male", "Some Other Race", 0.00029904],
    [30, "Female", "Some Other Race", 0.00033498],
    [30, "Nonbinary", "Some Other Race", 1.294e-05],
    [30, "Male", "White", 0.01564083],
    [30, "Female", "White", 0.01378558],
    [30, "Nonbinary", "White", 0.00060054],
    [40, "Male", "Asian", 0.02031423],
    [40, "Female", "Asian", 0.02480319],
    [40, "Nonbinary", "Asian", 0.00092076],
    [40, "Male", "Black", 0.00127956],
    [40, "Female", "Black", 0.00094255],
    [40, "Nonbinary", "Black", 4.535e-05],
    [40, "Male", "Hispanic", 0.00589193],
    [40, "Female", "Hispanic", 0.00524842],
    [40, "Nonbinary", "Hispanic", 0.00022735],
    [40, "Male", "Multiracial", 0.01344111],
    [40, "Female", "Multiracial", 0.01242465],
    [40, "Nonbinary", "Multiracial", 0.00052787],
    [40, "Male", "Pacific Islander", 0.00618012],
    [40, "Female", "Pacific Islander", 0.00577462],
    [40, "Nonbinary", "Pacific Islander", 0.00024397],
    [40, "Male", "Some Other Race", 0.0001424],
    [40, "Female", "Some Other Race", 0.00026717],
    [40, "Nonbinary", "Some Other Race", 8.36e-06],
    [40, "Male", "White", 0.01402969],
    [40, "Female", "White", 0.01134581],
    [40, "Nonbinary", "White", 0.00051787],
    [40, "Male", "Native American", 5.696e-05],
    [40, "Female", "Native American", 4.136e-05],
    [40, "Nonbinary", "Native American", 2.01e-06],
    [50, "Male", "Asian", 0.02451226],
    [50, "Female", "Asian", 0.02899764],
    [50, "Nonbinary", "Asian", 0.00026889],
    [50, "Male", "Black", 0.00114492],
    [50, "Female", "Black", 0.00056523],
    [50, "Nonbinary", "Black", 8.59e-06],
    [50, "Male", "Hispanic", 0.00391188],
    [50, "Female", "Hispanic", 0.00376455],
    [50, "Nonbinary", "Hispanic", 3.858e-05],
    [50, "Male", "Multiracial", 0.01075527],
    [50, "Female", "Multiracial", 0.01029399],
    [50, "Nonbinary", "Multiracial", 0.00010578],
    [50, "Male", "Native American", 6.54e-05],
    [50, "Female", "Native American", 4.131e-05],
    [50, "Nonbinary", "Native American", 5.4e-07],
    [50, "Male", "Pacific Islander", 0.00541343],
    [50, "Female", "Pacific Islander", 0.00494596],
    [50, "Nonbinary", "Pacific Islander", 5.206e-05],
    [50, "Male", "Some Other Race", 0.00011911],
    [50, "Female", "Some Other Race", 0.0001969],
    [50, "Nonbinary", "Some Other Race", 1.59e-06],
    [50, "Male", "White", 0.01412533],
    [50, "Female", "White", 0.01104029],
    [50, "Nonbinary", "White", 0.00012646],
    [60, "Male", "Asian", 0.02678146],
    [60, "Female", "Asian", 0.03107338],
    [60, "Nonbinary", "Asian", 0.00029073],
    [60, "Male", "Black", 0.00083856],
    [60, "Female", "Black", 0.00043718],
    [60, "Nonbinary", "Black", 6.41e-06],
    [60, "Male", "Hispanic", 0.00239656],
    [60, "Female", "Hispanic", 0.00298451],
    [60, "Nonbinary", "Hispanic", 2.704e-05],
    [60, "Male", "Multiracial", 0.00859967],
    [60, "Female", "Multiracial", 0.00843995],
    [60, "Nonbinary", "Multiracial", 8.563e-05],
    [60, "Male", "Native American", 5.095e-05],
    [60, "Female", "Native American", 4.337e-05],
    [60, "Nonbinary", "Native American", 4.7e-07],
    [60, "Male", "Pacific Islander", 0.00536455],
    [60, "Female", "Pacific Islander", 0.00556421],
    [60, "Nonbinary", "Pacific Islander", 5.492e-05],
    [60, "Male", "Some Other Race", 0.00023683],
    [60, "Female", "Some Other Race", 0.00017418],
    [60, "Nonbinary", "Some Other Race", 2.07e-06],
    [60, "Male", "White", 0.01654461],
    [60, "Female", "White", 0.01542447],
    [60, "Nonbinary", "White", 0.00016065],
    [70, "Male", "Asian", 0.0194052],
    [70, "Female", "Asian", 0.0243429],
    [70, "Nonbinary", "Asian", 0.00021984],
    [70, "Male", "Black", 0.00033253],
    [70, "Female", "Black", 0.00021343],
    [70, "Nonbinary", "Black", 2.74e-06],
    [70, "Male", "Hispanic", 0.0012358],
    [70, "Female", "Hispanic", 0.00129914],
    [70, "Nonbinary", "Hispanic", 1.274e-05],
    [70, "Male", "Multiracial", 0.00540724],
    [70, "Female", "Multiracial", 0.00528538],
    [70, "Nonbinary", "Multiracial", 5.373e-05],
    [70, "Male", "Native American", 6.2e-06],
    [70, "Female", "Native American", 0.00010327],
    [70, "Nonbinary", "Native American", 5.5e-07],
    [70, "Male", "Pacific Islander", 0.00327918],
    [70, "Female", "Pacific Islander", 0.00307746],
    [70, "Nonbinary", "Pacific Islander", 3.194e-05],
    [70, "Male", "White", 0.01420175],
    [70, "Female", "White", 0.01295837],
    [70, "Nonbinary", "White", 0.00013648],
    [70, "Male", "Some Other Race", 0.00015215],
    [70, "Female", "Some Other Race", 7.298e-05],
    [70, "Nonbinary", "Some Other Race", 1.13e-06],
    [80, "Male", "Asian", 0.00895905],
    [80, "Female", "Asian", 0.01364409],
    [80, "Nonbinary", "Asian", 0.00011358],
    [80, "Male", "Black", 0.00010465],
    [80, "Female", "Black", 0.00010602],
    [80, "Nonbinary", "Black", 1.06e-06],
    [80, "Male", "Hispanic", 0.00028296],
    [80, "Female", "Hispanic", 0.00049019],
    [80, "Nonbinary", "Hispanic", 3.89e-06],
    [80, "Male", "Multiracial", 0.00133907],
    [80, "Female", "Multiracial", 0.00186851],
    [80, "Nonbinary", "Multiracial", 1.612e-05],
    [80, "Male", "Pacific Islander", 0.00096317],
    [80, "Female", "Pacific Islander", 0.0013494],
    [80, "Nonbinary", "Pacific Islander", 1.162e-05],
    [80, "Male", "White", 0.00439312],
    [80, "Female", "White", 0.00445784],
    [80, "Nonbinary", "White", 4.448e-05],
    [90, "Male", "Asian", 0.00313598],
    [90, "Female", "Asian", 0.00611223],
    [90, "Nonbinary", "Asian", 4.647e-05],
    [90, "Male", "Black", 6.2e-06],
    [90, "Female", "Black", 0.00012048],
    [90, "Nonbinary", "Black", 6.4e-07],
    [90, "Male", "Hispanic", 2.685e-05],
    [90, "Female", "Hispanic", 0.00012186],
    [90, "Nonbinary", "Hispanic", 7.5e-07],
    [90, "Male", "Multiracial", 0.00014114],
    [90, "Female", "Multiracial", 0.00065542],
    [90, "Nonbinary", "Multiracial", 4e-06],
    [90, "Male", "Pacific Islander", 0.00015353],
    [90, "Female", "Pacific Islander", 0.00024372],
    [90, "Nonbinary", "Pacific Islander", 2e-06],
    [90, "Male", "White", 0.00063477],
    [90, "Female", "White", 0.00103959],
    [90, "Nonbinary", "White", 8.41e-06],
    [80, "Male", "Native American", 0.0],
    [80, "Female", "Native American", 2.203e-05],
    [80, "Nonbinary", "Native American", 1.1e-07],
    [80, "Male", "Some Other Race", 1.377e-05],
    [80, "Female", "Some Other Race", 7.986e-05],
    [80, "Nonbinary", "Some Other Race", 4.7e-07],
    [90, "Male", "Some Other Race", 1.79e-05],
    [90, "Female", "Some Other Race", 3.305e-05],
    [90, "Nonbinary", "Some Other Race", 2.6e-07]
]

# -----------------------------
# BUILD P(race | age, gender)
# -----------------------------


if __name__ == "__main__":
    hawaii_cond = defaultdict(lambda: defaultdict(float))
    hawaii_totals = defaultdict(float)

    for age, gender, race, prob in hawaii_data:
        key = (age, gender)
        hawaii_cond[key][race] += prob
        hawaii_totals[key] += prob

    # normalize
    for key in hawaii_cond:
        for race in hawaii_cond[key]:
            hawaii_cond[key][race] /= max(1/1e6,hawaii_totals[key])

    # -----------------------------
    # NONBINARY FUNCTION
    # -----------------------------

    def nb_rate(age):
        if age < 18:
            return 0.0
        elif age < 30:
            return 0.05
        elif age < 50:
            return 0.02
        else:
            return 0.005

    # -----------------------------
    # BUILD TERRITORY DATA
    # -----------------------------

    final = {}


    for territory in AGE_SEX:
        age_sex = AGE_SEX[territory]
        race_totals_raw = RACE_TOTALS[territory]

        # -----------------------------
        # Normalize targets
        # -----------------------------
        total_pop = sum(m+f for m,f in age_sex.values())
        target_age_sex = {}
        for age, (m, f) in age_sex.items():
            target_age_sex[(age, "Male")] = m / total_pop
            target_age_sex[(age, "Female")] = f / total_pop

        total_race = sum(race_totals_raw.values())
        target_race = {r: v / total_race for r, v in race_totals_raw.items()}

        # -----------------------------
        # Initialize joint using Hawaii
        # -----------------------------
        joint = defaultdict(float)

        for (age, gender), base_p in target_age_sex.items():
            hawaii_dist = hawaii_cond[(age, gender)]

            for race in target_race:
                p = base_p * hawaii_dist.get(race, 0)
                joint[(age, gender, race)] = p

        # -----------------------------
        # IPF / RAKING
        # -----------------------------
        for _ in range(ITERATIONS):

            # --- Fix race totals ---
            race_sums = defaultdict(float)
            for (a, g, r), v in joint.items():
                race_sums[r] += v

            for (a, g, r) in joint:
                if race_sums[r] > 0:
                    joint[(a, g, r)] *= target_race[r] / race_sums[r]

            # --- Fix age/sex totals ---
            ag_sums = defaultdict(float)
            for (a, g, r), v in joint.items():
                ag_sums[(a, g)] += v

            for (a, g, r) in joint:
                if ag_sums[(a, g)] > 0:
                    joint[(a, g, r)] *= target_age_sex[(a, g)] / ag_sums[(a, g)]

        # -----------------------------
        # Add nonbinary
        # -----------------------------
        for (age, gender, race), p in joint.items():
            nb = nb_rate(age)

            final[(territory, age, "Male", race)] = (
                    joint[(age, "Male", race)] * (1 - nb)
            )
            final[(territory, age, "Female", race)] = (
                    joint[(age, "Female", race)] * (1 - nb)
            )
            final[(territory, age, "Nonbinary", race)] = (
                    (joint[(age, "Male", race)] + joint[(age, "Female", race)]) * nb
            )

    # -----------------------------
    # NORMALIZE PER TERRITORY
    # -----------------------------

    totals = defaultdict(float)
    for (t, a, g, r), v in final.items():
        totals[t] += v

    for key in final:
        t = key[0]
        final[key] /= max(1/1e10,totals[t])

    # -----------------------------
    # EXPORT TS
    # -----------------------------

    state_maps = defaultdict(list)

    for (state, age, gender, race), prob in final.items():
        state_maps[state].append(([age, gender, race], round(prob, 8)))

    with open(OUTPUT_TS, "w") as f:
        f.write("export const demographics = {\n")
        for state, entries in state_maps.items():
            f.write(f'  "{state}": new Map([\n')
            for key, val in entries:
                f.write(f'    [[{key[0]}, "{key[1]}", "{key[2]}"], {val}],\n')
            f.write("  ]),\n")
        f.write("};\n")

