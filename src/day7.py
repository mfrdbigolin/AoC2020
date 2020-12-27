#!/bin/python3

# Copyright (C) 2020 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""Day Seven, Handy Haversacks."""

# I had to postpone this day because I was not aware of the techniques of
# graph theory to solve this problem.


from sys import argv
from re import findall

from utils import open_file, arrange, usage_and_exit, transfiged, dictf, \
    merge


def edges(graph):
    """Return the edges of a <graph>."""

    edge = []

    for vertex in graph:
        for neighbour in graph[vertex]:
            edge.append((vertex, neighbour))

    return edge


def solve1(bags, elem):
    """Return a set of ancestors of <elem> in the graph <bags>."""

    have = set()

    for edge in edges(bags):
        if edge[1] == elem:
            have |= solve1(bags, edge[0]) | {edge[0]}

    return have


def solve2(bags, elem):
    """Return the cumulative weight of elements from <elem> in <bags>."""

    count = 0

    for edge in edges(bags):
        if edge[0] == elem:
            count += edge[1][0] * solve2(bags, edge[1][1]) + edge[1][0]

    return count


# Capture the bag name and its contents (ignoring weights).
UNWEIGHTED_REG = r"(?:^|\d+ ?)(.+?) bags?"
# Capture the bag's contents and its weights.
WEIGHTED_REG = r"(\d+) (.+?) bags?"
# Capture the bag name.
VERTEX_REG = r"^(.+?) bags"


if __name__ == "__main__":
    usage_and_exit(len(argv) != 2)

    arranged_data = arrange(open_file(argv[1]))
    unweighted_data = merge([dictf(findall(UNWEIGHTED_REG, f))
                             for f in arranged_data])
    weighted_data = merge([dictf(findall(VERTEX_REG, f) + transfiged
                                 (findall(WEIGHTED_REG, f), (int, str)))
                        for f in arranged_data])

    print(len(solve1(unweighted_data, "shiny gold")))
    print(solve2(weighted_data, "shiny gold"))
