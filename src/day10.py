#!/bin/python3

# Copyright (C) 2020 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""Day Ten, Adapter Array."""


from sys import argv

from utils import open_file, arrange, usage_and_exit, diff


def solve1(voltage):
    """Multiply the group of one-difference with the group of three-difference
    <voltage>.  """

    diffs = diff(sorted(voltage + [0] + [max(voltage) + 3]))

    ones = len(list(filter(lambda a: a == 1, diffs)))
    threes = len(list(filter(lambda a: a == 3, diffs)))

    return ones*threes


def solve2(voltage):
    """Find the total number of possible arrangements of adapters considering
    the <voltage>.

    Reading the Python docs I discovered that there is a dictionary-like
    collection called Counter, suitable for counting objects.  Solving this
    challenge after the one from day 15, I attempted a solution with the
    Counter collection and one with an array, similar to what I did in
    'solve_fast' (vide day15.py); after doing some basic benchmarking I
    decided that the array method is definitely faster, and in this
    challenge the memory overhead is low, so I stuck with this technique.

    This section is getting quite long, but there is an interesting
    isomorphism between the group of one-differences in this puzzle and the
    Tribonacci sequence; while I was trying to find a method to solve in my
    notebook, I perceived that all possible permutations could be broken
    into Tribonacci factors, and the ones-group of differences form an
    'island'; counting the number of ones in each island, choosing the
    corresponding element of the sequence and multiplying with the number
    of the other islands gets the correct answer.  However, I decided to
    stay with the graph method (the one below), which itself is similar to
    the Tribonacci method.  """

    volts = sorted(voltage + [max(voltage) + 3])

    paths = [1] + [0] * volts[-1]

    for volt in volts:
        # The Tribonacci sequence creeps in.
        paths[volt] = paths[volt - 1] + paths[volt - 2] + paths[volt - 3]

    return paths[volts[-1]]


if __name__ == "__main__":
    usage_and_exit(len(argv) != 2)

    input_data = arrange(open_file(argv[1]), int)

    print(solve1(input_data))
    print(solve2(input_data))
