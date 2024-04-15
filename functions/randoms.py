from numpy import random

from data.geopolotical_areas import CONTINENTS_METATYPE_DISTRIBUTION as CONTINENTS
from data.geopolotical_areas import COUNTRIES, MEGACORPORATIONS
from data.metatypes import METATYPES, GENERAL_METATYPE_DISTRIBUTION

RNG = random.default_rng()


def determine_metatype(nation_or_megacorp: str = None):
    """
    Choose a random country or megacorporation to assign the SIN to.

    :param nation_or_megacorp: str, default = MEGACORP, continent code or MEGACORP
    :return: dict, random metatype
    """
    roll = RNG.uniform(0.0001, 100.0001)
    if nation_or_megacorp in MEGACORPORATIONS.keys():
        for metatype, rate in GENERAL_METATYPE_DISTRIBUTION.items():
            if roll in range(rate[0], rate[1]):
                return metatype, METATYPES[metatype]
        return "Human", METATYPES['Human']
    continent = COUNTRIES[nation_or_megacorp]['continent']
    for metatype, rate in CONTINENTS[continent].items():
        if roll in range(rate[0], rate[1]):
            return metatype, METATYPES[metatype]
    return "Human", METATYPES['Human']


def determine_metavariant(metatype: dict):
    """
    Randomly pick metavariant for a metatype based on ratios.

    :param metatype: dict, metatype
    :return: str, random metavariant
    """
    roll = RNG.uniform(0.0001, 100.0001)
    for metavariant, rate in metatype["Metavariants"].items():
        if rate[0] <= roll <= rate[1]:
            return metavariant
    return "Human"


def determine_country():
    """
    Randomly pick a country from list.

    :return: dict, random country
    """
    random_country: str = RNG.choice(list(COUNTRIES.keys()))
    return random_country, COUNTRIES[random_country]


def determine_megacorp():
    """
    Randomly pick a megacorp from list

    :return: dict, random megacorporation
    """
    random_megacorporation: str = RNG.choice(list(MEGACORPORATIONS.keys()))
    return random_megacorporation, MEGACORPORATIONS[random_megacorporation]


def determine_sin_origin():
    """
    Randomly determines if the SIN should originate from a country or megacorporation.
    :return: str, random country or megacorporation
    """
    roll = RNG.uniform(0.0001, 100.0001)
    if roll <= 13:
        return determine_megacorp()
    return determine_country()


def generate_sin_number():
    sin_number: str = ""
    for _ in range(1, 5):
        sin_number += str(RNG.integers(0, 10))
    return sin_number
