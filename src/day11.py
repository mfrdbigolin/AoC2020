#!/bin/python3

# Copyright (C) 2020 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""Day Eleven, Seating System."""

# In this challenge, the performance is not what I expected; I have
# attempted to optimize the code, but with only minor gains; so I will not
# attempt further, for I prefer readability over slight boosts.  Python is
# not a good language when it comes to performance in these cases.


from sys import argv
from enum import Enum
from re import sub
from copy import deepcopy

from utils import open_file, arrange, usage_and_exit


# 321
# 4.0
# 567

# .  .  .
#  3 2 1
#   321
# .44.00.
#   567
#  5 6 7
# .  .  .

# All the possible directions in a 2D-tile (vide the above diagrams for
# reference).
DIRECTIONS = [(0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1)]


# All the possible states for a tile.
State = Enum("State", "FREE OCC FLOOR", start=0)


def count_neighbours(grid, point, adjacent = True):
    """Count neighbours of <point> in <grid>.

    If <adjacent>, only adjacent points are considered; if not, any seat in
    the direction is taken into account.  """

    count = 0
    (size_row, size_col) = (len(grid), len(grid[point[0]]))

    for delta_row, delta_col in DIRECTIONS:
        (row, col) = (point[0] + delta_row, point[1] + delta_col)

        # The range built-in is much slower than chained comparisons here,
        # but I kept it for readability.
        if not adjacent:
            while row in range(size_row) and col in range(size_col) \
                  and grid[row][col] == State.FLOOR.value:
                row += delta_row
                col += delta_col

        if row in range(size_row) and col in range(size_col) \
           and grid[row][col] == State.OCC.value:
            count += 1

    return count


def solve(state, threshold, adjacent=True):
    """Find the number of occupied seats according to an initial <state>; a
    <threshold> is considered for the number of seats an occupied seat
    becomes a free one.

    The <adjacent> flag has the same meaning as in 'count_neighbours', vide
    supra for further reference.  """

    current = deepcopy(state)
    changed = True

    while changed:
        changed = False
        neighbours = [[count_neighbours(current, (row, seat), adjacent)
                       for seat in range(len(current[0]))]
                      for row in range(len(current))]

        for i, row in enumerate(current):
            for j, seat in enumerate(row):
                if seat == State.FREE.value and neighbours[i][j] == 0:
                    current[i][j] = State.OCC.value
                    changed = True
                elif seat == State.OCC.value \
                     and neighbours[i][j] >= threshold:
                    current[i][j] = State.FREE.value
                    changed = True

    return sum([row.count(State.OCC.value) for row in current])


# Replace all the symbols in <st> with numbers.
enumer = lambda st: sub(r"[.]", "2", sub(r"#", "1", sub(r"L", "0", st)))


if __name__ == "__main__":
    usage_and_exit(len(argv) != 2)

    input_data = [[int(i) for i in list(enumer(row))]
                  for row in arrange(open_file(argv[1]))]

    print(solve(input_data, 4))
    print(solve(input_data, 5, False))
