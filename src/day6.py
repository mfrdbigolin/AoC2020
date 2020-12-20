#!/bin/python3

# Copyright (C) 2020 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""Day Six, Custom Customs."""


from sys import argv
from re import sub

from utils import open_file, arrange, usage_and_exit


def solve(grps, freq_rule = None):
    """Return the sum of positive questions answered by the groups <grps>
    according to a frequency rule <freq_rule>.

    The <freq_rule> is a function that receives a frequency <f> and a group
    <g>; it defaults to None, meaning that if no rule is given any positive
    answer will count.  """

    n_ques = 0

    for grp in grps:
        # Group without distinction to individual person.
        sub_g = sub(r"\s", "", grp)
        letters = {}

        for question in sub_g:
            if question not in letters.keys():
                letters[question] = 0
            letters[question] += 1

        for freq in letters.values():
            n_ques += freq_rule(freq, grp) if freq_rule is not None else 1

    return n_ques


# Require every person to answer "yes" to the same question.
allYes = lambda f, g: 1 if f == len(g.split("\n")) else 0


if __name__ == "__main__":
    usage_and_exit(len(argv) != 2)

    input_data = arrange(open_file(argv[1]), sep="\n\n")

    print(solve(input_data))
    print(solve(input_data, allYes))
