import {demographics} from "./demographics";
import {Affiliation, Gender, Race, State, statePopulations} from "./constants";
import {names} from "./names"
import {namesByRace} from "./names_by_race";
import {inferPartyDist, sampleParty} from "./politics";
import {locationsByState} from "./locations_by_state";
import {nb_names} from "./nb_names";

export type UsLocation = {
    state: State;
    x: number;
    y: number;
}

export type Person = {
    firstName: string;
    gender: Gender
    age: number;
    race: Race;
    location: UsLocation;
    politicalAffiliation: Affiliation | "Not Voted";
}

function getWeightedKey<K>(keys: Map<K, number>): K {
    const keySum = Array.from(keys.values()).reduce((acc, val) => acc + val, 0);

    const random = Math.random() * keySum;
    let acc = 0;

    for (const [key, value] of keys.entries()) {
        acc += value;
        if (acc > random) {
            return key;
        }
    }

    return Array.from(keys.keys())[0];
}

function combineNameDists(stateDist: Map<string, number>, raceDist: Map<string, number>) {
    const combined = new Map<string, number>();

    for (const [name, p1] of stateDist.entries()) {
        const p2 = raceDist.get(name) ?? 0.0000001;
        combined.set(name, p1 * p2);
    }

    let total = 0;
    for (const v of combined.values()) total += v;

    for (const k of combined.keys()) {
        combined.set(k, combined.get(k)! / total);
    }

    return combined;
}

export function generateRandomPerson() : Person {
    // Pick random state by population

    console.log(statePopulations);
    const state = getWeightedKey(statePopulations);

    // Pick gender, race, age, education

    const [ageBracket, gender, race] = getWeightedKey(demographics[state]);
    const age = ageBracket + Math.floor(Math.random() * 10)
    console.log(age, gender, race);

    // Pick political affiliation

    let party
    if (age >= 18) {
        const dist = inferPartyDist(age, race, gender, state);
        party = sampleParty(dist);
    } else {
        party = "Not Voted"
    }

    // Pick name

    const birthYear = Math.min(2019, 2026 - age);
    const decade = Math.floor(birthYear / 10) * 10;

    let name;
    if (gender === "Nonbinary") {
        name = nb_names[Math.floor(nb_names.length * Math.random())];
    } else {
        const genderKey = gender[0];
        console.log(ageBracket, gender, race, decade);

        const stateNameDist = names[state]
            .get(genderKey)
            ?.get(decade)
        if (race == "Some Other Race" || race == "Pacific Islander") {
            const otherRaces = ["White","Black", "Native American", "Asian", "Multiracial", "Hispanic"]
            race = otherRaces[Math.floor(Math.random() * otherRaces.length)]
        }
        name = getWeightedKey(combineNameDists(stateNameDist, namesByRace[race]));
    }

    const locations = locationsByState[state]
    const location = locations[Math.floor(locations.length * Math.random())];

    return {
        firstName: name,
        gender: gender,
        age: age,
        race: race,
        location: {
            state: state,
            x: location[0],
            y: location[1],
        },
        politicalAffiliation: party
    };
}


