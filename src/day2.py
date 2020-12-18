#!/bin/python3

# Copyright (C) 2020 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""Day Two, Password Philosophy."""


from sys import argv

from utils import open_file, arrange, usage_and_exit, regex


# Regular expression to match the password's fields.
FORM = r"(\d+)-(\d+) ([a-zA-Z]{1}): ([a-zA-Z]+)"


# Individual policies for each case.
pol1 = lambda p: p[3].count(p[2]) in range(p[0], p[1] + 1)
pol2 = lambda p: (p[3][p[0] - 1] == p[2]) != (p[3][p[1] - 1] == p[2])


def solve(pwds, policy):
    """Filter the passwords <pwds> according to <policy> and return the
    number of accepted ones.  """

    return len(list(filter(policy, pwds)))


if __name__ == "__main__":
    usage_and_exit(len(argv) != 2)

    arranged_data = arrange(open_file(argv[1]))
    matched_data = regex(arranged_data, (int, int, str, str), FORM)

    print(solve(matched_data, pol1))
    print(solve(matched_data, pol2))
