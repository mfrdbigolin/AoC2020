#!/bin/python3

# Copyright (C) 2021 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""Day Twenty-Four, Lobby Layout."""


from sys import argv
from re import findall
from copy import deepcopy

from utils import open_file, arrange, usage_and_exit


# All possible directions in a hextille.
DIRECTIONS = [(2,0), (1,1), (-1,1), (-2,0), (-1,-1), (1,-1)]

# All possible cardinals, directly correspondent with 'DIRECTIONS'.
CARDINALS = ["e", "ne", "nw", "w", "sw", "se"]


def solve1(lines):
    """Flip hextilles according to <lines>' directions and return a set
    with the black tiles.  """

    blacks = set()

    for directions in lines:
        point = (0,0)

        for cardinal in directions:
            (delta_row, delta_col) = DIRECTIONS[CARDINALS.index(cardinal)]

            point = (point[0] + delta_row, point[1] + delta_col)

        if point not in blacks:
            blacks.add(point)
        else:
            blacks.remove(point)

    return blacks


def count_neighbours(grid, point):
    """Count neighbours adjacent to <point> in the hextille <grid>."""
    count = 0

    for delta_row, delta_col in DIRECTIONS:
        neighbour = (point[0] + delta_row, point[1] + delta_col)

        if neighbour in grid:
            count += 1

    return count


def ground(blacks):
    """Generate the ground of the figure <blacks>, i.e., obtain all white
    tiles immediately adjacent to <blacks>.  """

    whites = set()

    for black in blacks:
        for delta_row, delta_col in DIRECTIONS:
            (row, col) = (black[0] + delta_row, black[1] + delta_col)

            if (row, col) not in whites and (row, col) not in blacks:
                whites.add((row,col))

    return whites


def solve2(blacks, times):
    """Flip the hextilles <times> times, initialy start with <blacks> grid.
    Return the final tiles, for symmetry with 'solve1'.  """

    current = deepcopy(blacks)

    for _ in range(times):
        prev = deepcopy(current)
        whites = ground(current)

        for black in prev:
            neigh_b = count_neighbours(prev, black)

            if neigh_b not in [1,2]:
                current.remove(black)

        for white in whites:
            neigh_w = count_neighbours(prev, white)

            if neigh_w == 2:
                current.add(white)

    return current


# Extract the individual cardinals from the direction.
CARD_REG = r"(ne|nw|se|sw|e|w)"


if __name__ == "__main__":
    usage_and_exit(len(argv) != 2)

    input_data = [findall(CARD_REG, tile)
                  for tile in arrange(open_file(argv[1]))]

    print(len(sol := solve1(input_data)))
    print(len(solve2(sol, 100)))
