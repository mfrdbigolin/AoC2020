#!/bin/python3

# Copyright (C) 2020 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""Day Nine, Encoding Error."""


from sys import argv

from utils import open_file, arrange, usage_and_exit


# Generate all possible unique double sums in a list <ls>.
two_sum = lambda ls: [i+j for j in ls for i in ls if j < i]


def solve1(lst, pre):
    """In a list <lst> find the first element that sum does not have in its
    summands the preceding <pre> elements (excluding the preamble).

    The first <pre> elements are the preamble and are the building blocks
    of the next elements.  """

    bad_elem = None

    for i, elem in enumerate(lst[pre:]):
        if elem not in two_sum(lst[i:pre + i]):
            bad_elem = elem

    return bad_elem


# Cumulatively sum all elements of the list <ls> through <i>.
cum_sum = lambda ls, i: sum(ls[:i + 1])


def solve2(lst, k):
    """Find in a list <lst> a group of any size whose sum equals <k>."""

    for i in range(len(lst)):
        for j in range(len(lst)):
            if i > j and cum_sum(lst, i) - cum_sum(lst, j) == k:
                part = lst[j + 1:i + 1]

                return min(part) + max(part)

    return None


if __name__ == "__main__":
    usage_and_exit(len(argv) != 2)

    input_data = arrange(open_file(argv[1]), int)

    print(sol1 := solve1(input_data, 25))
    print(solve2(input_data, sol1))
