import {Gender, Affiliation, Race, State} from "./constants"

export const byGender: Record<Gender, Record<Affiliation, number>> = {
    Male: { Democrat: 0.388728, Republican: 0.434748, Independent: 0.176524},
    Female: { Democrat: 0.461193, Republican: 0.351213, Independent: 0.187594},
    Nonbinary: { Democrat: 0.424961, Republican: 0.392981, Independent: 0.182059},
};

export const byAgeGender: Record<number, Record<Gender, Record<Affiliation, number>>> = {
    18: {
        Male: { Democrat: 0.461538, Republican: 0.471154, Independent: 0.067308,  },
        Female: { Democrat: 0.575472, Republican: 0.358491, Independent: 0.066038,  },
        Nonbinary: { Democrat: 0.518505, Republican: 0.414822, Independent: 0.066673,  },
    },
    30: {
        Male: { Democrat: 0.416667, Republican: 0.481481, Independent: 0.101852,  },
        Female: { Democrat: 0.513761, Republican: 0.376147, Independent: 0.110092,  },
        Nonbinary: { Democrat: 0.465214, Republican: 0.428814, Independent: 0.105972,  },
    },
    45: {
        Male: { Democrat: 0.342105, Republican: 0.517544, Independent: 0.140351,  },
        Female: { Democrat: 0.415254, Republican: 0.423729, Independent: 0.161017,  },
        Nonbinary: { Democrat: 0.37868, Republican: 0.470637, Independent: 0.150684,  },
    },
    65: {
        Male: { Democrat: 0.387387, Republican: 0.504505, Independent: 0.108108,  },
        Female: { Democrat: 0.46087, Republican: 0.4, Independent: 0.13913,  },
        Nonbinary: { Democrat: 0.424129, Republican: 0.452253, Independent: 0.123619,  },
    },
};

export const byRaceGender: Record<Race, Record<Gender, Record<Affiliation, number>>> = {
    "White": {
        Male: { Democrat: 0.287879, Republican: 0.454545, Independent: 0.257576,  },
        Female: { Democrat: 0.338235, Republican: 0.389706, Independent: 0.272059,  },
        Nonbinary: { Democrat: 0.313057, Republican: 0.422125, Independent: 0.264818,  },
    },
    "Black": {
        Male: { Democrat: 0.747573, Republican: 0.203883, Independent: 0.048544,  },
        Female: { Democrat: 0.867925, Republican: 0.066038, Independent: 0.066038,  },
        Nonbinary: { Democrat: 0.807749, Republican: 0.134961, Independent: 0.057291,  },
    },
    "Hispanic": {
        Male: { Democrat: 0.423077, Republican: 0.519231, Independent: 0.057692,  },
        Female: { Democrat: 0.563107, Republican: 0.378641, Independent: 0.058252,  },
        Nonbinary: { Democrat: 0.493092, Republican: 0.448936, Independent: 0.057972,  },
    },
    "Asian": {
        Male: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        Female: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        Nonbinary: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
    },
    "Native American": {
        Male: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        Female: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        Nonbinary: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
    },
    "Pacific Islander": {
        Male: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        Female: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        Nonbinary: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
    },
    "Some Other Race": {
        Male: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        Female: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        Nonbinary: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
    },
    "Multiracial": {
        Male: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        Female: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        Nonbinary: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
    },
};

export const byState: Record<State, Record<Affiliation, number>> = {
    "Alaska": { Democrat: 0.121512, Republican: 0.238124, Independent: 0.640364,  },
    "Alabama": { Democrat: 0.361836, Republican: 0.552155, Independent: 0.086009,  },
    "Arkansas": { Democrat: 0.207221, Republican: 0.379938, Independent: 0.412841,  },
    "American Samoa": { Democrat: 0.55, Republican: 0.35, Independent: 0.1,  },
    "Arizona": { Democrat: 0.285, Republican: 0.356, Independent: 0.359,  },
    "California": { Democrat: 0.447061, Republican: 0.253568, Independent: 0.299371,  },
    "Colorado": { Democrat: 0.2529, Republican: 0.2277, Independent: 0.5194,  },
    "Connecticut": { Democrat: 0.352165, Republican: 0.208779, Independent: 0.439056,  },
    "District of Columbia": { Democrat: 0.7508, Republican: 0.0526, Independent: 0.1966,  },
    "Delaware": { Democrat: 0.4251, Republican: 0.2565, Independent: 0.3184,  },
    "Florida": { Democrat: 0.315468, Republican: 0.383062, Independent: 0.30147,  },
    "Georgia": { Democrat: 0.4308, Republican: 0.2685, Independent: 0.3007,  },
    "Guam": { Democrat: 0.46, Republican: 0.43, Independent: 0.11,  },
    "Hawaii": { Democrat: 0.3787, Republican: 0.1364, Independent: 0.4849,  },
    "Iowa": { Democrat: 0.2821, Republican: 0.3701, Independent: 0.3478,  },
    "Idaho": { Democrat: 0.1179, Republican: 0.4634, Independent: 0.4187,  },
    "Illinois": { Democrat: 0.377038, Republican: 0.275328, Independent: 0.347635,  },
    "Indiana": { Democrat: 0.25, Republican: 0.3094, Independent: 0.4406,  },
    "Kansas": { Democrat: 0.2506, Republican: 0.4563, Independent: 0.2931,  },
    "Kentucky": { Democrat: 0.4176, Republican: 0.4773, Independent: 0.1051,  },
    "Louisiana": { Democrat: 0.3681, Republican: 0.3538, Independent: 0.2781,  },
    "Massachusetts": { Democrat: 0.2574, Republican: 0.0837, Independent: 0.6589,  },
    "Maryland": { Democrat: 0.5174, Republican: 0.2388, Independent: 0.2438,  },
    "Maine": { Democrat: 0.333167, Republican: 0.286671, Independent: 0.380162,  },
    "Michigan": { Democrat: 0.38, Republican: 0.45, Independent: 0.17,  },
    "Minnesota": { Democrat: 0.3392, Republican: 0.3782, Independent: 0.2826,  },
    "Missouri": { Democrat: 0.335, Republican: 0.4688, Independent: 0.1962,  },
    "Northern Mariana Islands": { Democrat: 0.33, Republican: 0.4, Independent: 0.27,  },
    "Mississippi": { Democrat: 0.2365, Republican: 0.2924, Independent: 0.4711,  },
    "Montana": { Democrat: 0.2645, Republican: 0.4476, Independent: 0.2879,  },
    "North Carolina": { Democrat: 0.306151, Republican: 0.305054, Independent: 0.388795,  },
    "North Dakota": { Democrat: 0.287171, Republican: 0.427057, Independent: 0.285771,  },
    "Nebraska": { Democrat: 0.2617, Republican: 0.4988, Independent: 0.2395,  },
    "New Hampshire": { Democrat: 0.2827, Republican: 0.3204, Independent: 0.3969,  },
    "New Jersey": { Democrat: 0.3862, Republican: 0.2534, Independent: 0.3604,  },
    "New Mexico": { Democrat: 0.437506, Republican: 0.328946, Independent: 0.233548,  },
    "Nevada": { Democrat: 0.289029, Republican: 0.283328, Independent: 0.427643,  },
    "New York": { Democrat: 0.4738, Republican: 0.2279, Independent: 0.2983,  },
    "Ohio": { Democrat: 0.310669, Republican: 0.307169, Independent: 0.382162,  },
    "Oklahoma": { Democrat: 0.258474, Republican: 0.539446, Independent: 0.20208,  },
    "Oregon": { Democrat: 0.349128, Republican: 0.257161, Independent: 0.393711,  },
    "Pennsylvania": { Democrat: 0.439004, Republican: 0.423231, Independent: 0.137765,  },
    "Puerto Rico": { Democrat: 0.395, Republican: 0.347, Independent: 0.258,  },
    "Rhode Island": { Democrat: 0.360036, Republican: 0.144514, Independent: 0.49545,  },
    "South Carolina": { Democrat: 0.4103, Republican: 0.4913, Independent: 0.0984,  },
    "South Dakota": { Democrat: 0.270286, Republican: 0.600872, Independent: 0.128842,  },
    "Tennessee": { Democrat: 0.181918, Republican: 0.337334, Independent: 0.480748,  },
    "Texas": { Democrat: 0.4652, Republican: 0.3775, Independent: 0.1573,  },
    "Utah": { Democrat: 0.136314, Republican: 0.515752, Independent: 0.347935,  },
    "Virginia": { Democrat: 0.518048, Republican: 0.29987, Independent: 0.182082,  },
    "U.S. Virgin Islands": { Democrat: 0.6732, Republican: 0.0349, Independent: 0.2919,  },
    "Vermont": { Democrat: 0.53, Republican: 0.2025, Independent: 0.2675,  },
    "Washington": { Democrat: 0.5228, Republican: 0.276, Independent: 0.2012,  },
    "Wisconsin": { Democrat: 0.311769, Republican: 0.370863, Independent: 0.317368,  },
    "West Virginia": { Democrat: 0.282672, Republican: 0.423758, Independent: 0.293571,  },
    "Wyoming": { Democrat: 0.1226, Republican: 0.7523, Independent: 0.1251,  },
};

export const byRaceAge: Record<Race, Record<number, Record<Affiliation, number>>> = {
    "White": {
        18: { Democrat: 0.462264, Republican: 0.462264, Independent: 0.075472,  },
        30: { Democrat: 0.389381, Republican: 0.477876, Independent: 0.132743,  },
        45: { Democrat: 0.300813, Republican: 0.495935, Independent: 0.203252,  },
        65: { Democrat: 0.352459, Republican: 0.459016, Independent: 0.188525,  },
    },
    "Black": {
        18: { Democrat: 0.821782, Republican: 0.158416, Independent: 0.019802,  },
        30: { Democrat: 0.821782, Republican: 0.148515, Independent: 0.029703,  },
        45: { Democrat: 0.823529, Republican: 0.137255, Independent: 0.039216,  },
        65: { Democrat: 0.911765, Republican: 0.058824, Independent: 0.029412,  },
    },
    "Hispanic": {
        18: { Democrat: 0.520408, Republican: 0.459184, Independent: 0.020408,  },
        30: { Democrat: 0.52, Republican: 0.45, Independent: 0.03,  },
        45: { Democrat: 0.495146, Republican: 0.466019, Independent: 0.038835,  },
        65: { Democrat: 0.574257, Republican: 0.405941, Independent: 0.019802,  },
    },
    "Asian": {
        18: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        30: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        45: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        65: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
    },
    "Native American": {
        18: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        30: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        45: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        65: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
    },
    "Pacific Islander": {
        18: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        30: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        45: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        65: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
    },
    "Some Other Race": {
        18: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        30: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        45: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        65: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
    },
    "Multiracial": {
        18: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        30: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        45: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
        65: { Democrat: 0.480392, Republican: 0.460784, Independent: 0.058824,  },
    },
};

const PARTIES: Affiliation[] = ["Democrat", "Republican", "Independent"];
const EPS = 1e-9;

const AGE_BUCKETS = [18, 30, 45, 65];

// Approximate US gender distribution for marginalizing gender out of race×gender
const GENDER_WEIGHTS: Record<Gender, number> = {
    Male: 0.49,
    Female: 0.50,
    Nonbinary: 0.01,
};

function safeLog(p: number): number {
    return Math.log(Math.max(p, EPS));
}

function softmax(scores: Record<Affiliation, number>): Record<Affiliation, number> {
    const max = Math.max(...PARTIES.map((p) => scores[p]));
    const exps = Object.fromEntries(
        PARTIES.map((p) => [p, Math.exp(scores[p] - max)])
    ) as Record<Affiliation, number>;
    const sum = PARTIES.reduce((s, p) => s + exps[p], 0);
    return Object.fromEntries(
        PARTIES.map((p) => [p, exps[p] / sum])
    ) as Record<Affiliation, number>;
}

function ageBucket(age: number): number {
    let bucket = AGE_BUCKETS[0];
    for (const b of AGE_BUCKETS) {
        if (age >= b) bucket = b;
    }
    return bucket;
}

/** P(party | race): marginalize byRaceGender over gender using population weights */
function marginalizeGender(race: Race): Record<Affiliation, number> {
    const result = Object.fromEntries(PARTIES.map((p) => [p, 0])) as Record<Affiliation, number>;
    for (const [gender, w] of Object.entries(GENDER_WEIGHTS) as [Gender, number][]) {
        for (const p of PARTIES) {
            result[p] += w * byRaceGender[race][gender][p];
        }
    }
    const total = PARTIES.reduce((s, p) => s + result[p], 0);
    return Object.fromEntries(PARTIES.map((p) => [p, result[p] / total])) as Record<Affiliation, number>;
}

// Cache P(party | race) per race — computed once at module load
const raceOnlyCache = new Map<Race, Record<Affiliation, number>>();
function getRaceOnly(race: Race): Record<Affiliation, number> {
    if (!raceOnlyCache.has(race)) raceOnlyCache.set(race, marginalizeGender(race));
    return raceOnlyCache.get(race)!;
}

/** National prior P(party): marginalize byGender over gender */
const nationalPrior: Record<Affiliation, number> = (() => {
    const result = Object.fromEntries(PARTIES.map((p) => [p, 0])) as Record<Affiliation, number>;
    for (const [gender, w] of Object.entries(GENDER_WEIGHTS) as [Gender, number][]) {
        for (const p of PARTIES) {
            result[p] += w * byGender[gender][p];
        }
    }
    const total = PARTIES.reduce((s, p) => s + result[p], 0);
    return Object.fromEntries(PARTIES.map((p) => [p, result[p] / total])) as Record<Affiliation, number>;
})();

export function inferPartyDist(
    age: number,
    race: Race,
    gender: Gender,
    state: string
): Record<Affiliation, number> {
    const bucket = ageBucket(age);

    const raceGender = byRaceGender[race][gender];  // P(party | race, gender)
    const raceAge    = byRaceAge[race][bucket];     // P(party | race, age)
    const raceOnly   = getRaceOnly(race);           // P(party | race)  — dedup anchor
    const stDist     = byState[state];              // P(party | state)

    const scores = Object.fromEntries(
        PARTIES.map((party) => [
            party,
            safeLog(raceGender[party])       // P(party | race, gender)
            + safeLog(raceAge[party])        // P(party | race, age)
            - safeLog(raceOnly[party])       // − P(party | race)        [dedup race]
            + safeLog(stDist[party])         // P(party | state)
            - safeLog(nationalPrior[party]), // − P(party)               [center state]
        ])
    ) as Record<Affiliation, number>;

    return softmax(scores);
}

export function sampleParty(dist: Record<Affiliation, number>): Affiliation {
    let r = Math.random();
    for (const party of PARTIES) {
        r -= dist[party];
        if (r <= 0) return party;
    }
    return PARTIES[PARTIES.length - 1];
}