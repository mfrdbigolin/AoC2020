#!/bin/python3

# Copyright (C) 2020 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""Day One, Report Repair."""


from sys import argv

from utils import open_file, arrange, usage_and_exit


def solve(lst, num, k):
    """In a list <lst> find <num> numbers whose sum amount to <k> and obtain
    the product of them.

    Recursive generalized 3SUM (k-SUM) algorithm.  """

    # 1SUM.
    if num == 1:
        return k if k in lst else None

    # Sort list for binary search.
    sorted_lst = sorted(lst)

    for i, head in enumerate(sorted_lst[:-1]):
        if (tail := solve(sorted_lst[i + 1:], num - 1, k - head)) \
           is not None:
            return head*tail

    return None


if __name__ == "__main__":
    usage_and_exit(len(argv) != 2)

    input_data = arrange(open_file(argv[1]), int)

    print(solve(input_data, 2, 2020))
    print(solve(input_data, 3, 2020))
