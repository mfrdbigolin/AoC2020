#!/bin/python3

# Copyright (C) 2021 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""Day Twenty-One, Allergen Assessment."""


from sys import argv
from re import findall
from collections import defaultdict
from functools import reduce

from utils import open_file, arrange, usage_and_exit, freqd2


def gen_allergen(recipes):
    """From a list of <recipes> group together similar allergens
    ingredients.  """

    grouped_aller = defaultdict(list)
    groups = [{aller: recipe[0] for aller in recipe[1]}
             for recipe in recipes]

    for dictionary in groups:
        for key, elem in dictionary.items():
            grouped_aller[key] += [elem]

    return grouped_aller


def intersect(groups):
    """Given <groups> of allergens grouped with ingredients, find the allergen
    contained in each of the relevant ingredients.  """

    intersecs = {k: reduce(lambda a, b: a.intersection(b), e)
                 for k, e in groups.items()}

    inert = False
    found = set()
    while not inert:
        inert = True

        for key, elem in intersecs.items():
            if isinstance(elem, set):
                inert = False

                if len(elem) == 1:
                    intersecs[key] = [*elem][0]
                    found |= elem
                else:
                    intersecs[key] = elem.difference(found)

    return intersecs


def solve1(freq, groups):
    """Count the number of occurrences of ingredients without allergens given
    the frequency <freq> and the <groups>.  """

    intersecs = intersect(groups)

    return sum([freq[k] for k in set(freq.keys())
                .difference(set(intersecs.values()))])


def solve2(groups):
    """Return an alphabetical list with the ingredients arranged according to
    their allergens given the <groups>.  """

    intersecs = intersect(groups)

    return ",".join([intersecs[a] for a in sorted(intersecs.keys())])


# Extract the ingredients.
INGR_REG = r"(?<!\()\b(\w+) "
# Get the allergens.
ALLER_REG = r"(?:(\w+)(?:, |\)))"


if __name__ == "__main__":
    usage_and_exit(len(argv) != 2)

    input_data = arrange(open_file(argv[1]))

    ingredients = [set(findall(INGR_REG, recipe))
                   for recipe in input_data]
    allergens = [set(findall(ALLER_REG, recipe)) for recipe in input_data]

    recipe = list(zip(ingredients, allergens))

    freq_data = freqd2(ingredients)
    group_data = gen_allergen(recipe)

    print(solve1(freq_data, group_data))
    print(solve2(group_data))
