#!/bin/python3

# Copyright (C) 2020 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""Day Three, Toboggan Trajectory."""


from sys import argv

from utils import open_file, arrange, usage_and_exit, product


def solve(terrain, slopes):
    """Return the product of the number of trees for each <slopes>,
    according to the <terrain>.  """

    return product(map(lambda s: tree(terrain, s), slopes))


def tree(terrain, slope):
    """Calculate the number of trees for a <terrain> and a particular
    <slope>.  """

    trees = 0

    for i, _ in enumerate(terrain):
        if slope[0]*i <= len(terrain) \
           and terrain[slope[0] * i][slope[1]*i % len(terrain[0])] == "#":
            trees += 1

    return trees


SLOPES = [(1,1), (1,3), (1,5), (1,7), (2,1)]


if __name__ == "__main__":
    usage_and_exit(len(argv) != 2)

    input_data = arrange(open_file(argv[1]))

    print(solve(input_data, [SLOPES[1]]))
    print(solve(input_data, SLOPES))
