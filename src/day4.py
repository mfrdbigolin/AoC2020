#!/bin/python3

# Copyright (C) 2020 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""Day Four, Passport Processing."""


from sys import argv
from re import findall, match

from utils import open_file, arrange, assoc, usage_and_exit


def hgt(height):
    """Check the <height>.

    I would prefer this verification to be contained in a lambda function
    similar to the other cases, but this logic would be too convoluted in
    an anonymous expression.  """

    if match(r"\d+(?:cm|in)$", height) is None:
        return False

    num = int(findall(r"^(\d+)", height)[0])
    unit = findall(r"(cm|in)$", height)[0]

    in_range = False
    if unit == "cm":
        in_range = num in range(150, 193+1)
    elif unit == "in":
        in_range = num in range(59, 76+1)

    return in_range


# Grand dictionary of rules.
RULEBOOK = {"byr": lambda v: (match(r"\d{4}$", v) is not None) \
                             and (int(v) in range(1920, 2002+1)),
            "iyr": lambda v: (match(r"\d{4}$", v) is not None) \
                             and (int(v) in range(2010, 2020+1)),
            "eyr": lambda v: (match(r"\d{4}$", v) is not None) \
                             and (int(v) in range(2020, 2030+1)),
            "hgt": hgt, # Vide supra.
            "hcl": lambda v: match(r"#[0-9a-f]{6}$", v) is not None,
            "ecl": lambda v: v in ["amb", "blu", "brn", "gry",
                                   "grn", "hzl", "oth"],
            "pid": lambda v: match(r"\d{9}$", v) is not None}


# Capture in a group only the key name.
KEY_REG = r"(\w{3}):.+?(?:\s|$)"
# Capture key and value.
KEY_VAL_REG = r"(\w{3}):(.+?)(?:\s|$)"
REQ_KEYS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def solve(passes, rules = None):
    """Validate the passports <passes> according to <rules> and check the
    required fields (<REQ_KEYS>); if no <rules> are provided, check only
    the required fields.  """

    valid = 0

    for pasp in passes:
        # Dictionary association with {key: value}.
        soc = dict(findall(KEY_VAL_REG, pasp))
        keys = set(findall(KEY_REG, pasp))

        if keys.issuperset(REQ_KEYS) \
           and (rules is None or assoc(soc, rules)):
            valid += 1

    return valid


if __name__ == "__main__":
    usage_and_exit(len(argv) != 2)

    input_data = arrange(open_file(argv[1]), sep="\n\n")

    print(solve(input_data))
    print(solve(input_data, RULEBOOK))
