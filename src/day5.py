#!/bin/python3

# Copyright (C) 2020 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""Day Five, Binary Boarding."""

# The first part of the puzzle was so easy that I solved it without code; I
# just used NeoVim's search function and filtered down the possibilities.
# So I will only provide a solution for the second part.


from sys import argv
from re import sub

from utils import open_file, arrange, usage_and_exit


def solve(seats):
    """Find the missing seat from the occupied <seats>.

    I used my own implementation of insertion sort to solve this one.  """

    sort_s = [False] * 2**10

    for i in seats:
        sort_s[i] = True

    our_s = 0
    for i, _ in enumerate(sort_s):
        if not sort_s[i] and sort_s[i - 1] and sort_s[i + 1]:
            our_s = i
            break

    return our_s


# Transform the seat ID <s> in a binary number.
binnum = lambda s: int(sub("(?:F|L)", "0", sub("(?:B|R)", "1", s)), 2)


if __name__ == "__main__":
    usage_and_exit(len(argv) != 2)

    input_data = [binnum(seat) for seat in arrange(open_file(argv[1]))]

    print(solve(input_data))
