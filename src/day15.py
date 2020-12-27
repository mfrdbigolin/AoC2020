#!/bin/python3

# Copyright (C) 2020 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""Day Fifteen, Rambunctious Recitation."""

# Gladly, I already knew Van Eck's sequence before this challenge, so this
# one was not so hard.  My original solution (solve) took 13 seconds to run
# both parts of the program, following a piece of advice on Justin Le's
# (mstksg) Advent of Code 2020 Reflections I tried to build a solution
# (solve_fast) that stored the previous values on an array, instead of a
# dictionary; however, the performance gain is negligible (both parts took
# 10 seconds) and the memory use is high; therefore I still maintain solve
# as the default.


from sys import argv
from functools import reduce

from utils import open_file, arrange, usage_and_exit


def solve(k, lim):
    """Find the <lim>th term of a Van Eck's sequence with initial values
    <k>.  """

    seq = [*k]
    nums = reduce(lambda a, b: a | b, [{n: i} for i,n in enumerate(seq)])

    for i in range(len(k) - 1, lim):
        res = nums.get(seq[i], i)

        seq.append(i-res)
        nums[seq[i]] = i

    return seq[lim - 1]


def solve_fast(k, lim):
    """A little faster version of 'solve', but with a high memory usage.  This
    version uses an array to store all the previous values, it uses the
    value as the index and the previous index as the element.  """

    seq = [*k]
    nums = [None] * (max(seq) + 1)

    for i, elem in enumerate(seq):
        nums[elem] = i

    for i in range(len(k) - 1, lim):
        res = nums[seq[i]] if nums[seq[i]] is not None else i

        seq.append(i-res)
        nums.append(None)
        nums[seq[i]] = i

    return seq[lim - 1]


if __name__ == "__main__":
    usage_and_exit(len(argv) != 2)

    input_data = arrange(open_file(argv[1]), int, ",")

    print(solve(input_data, 2020))
    print(solve(input_data, 30000000))
