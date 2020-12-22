#!/bin/python3

# Copyright (C) 2020 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""Day Eight, Handheld Halting."""


from sys import argv

from utils import open_file, arrange, usage_and_exit, regex


def solve1(ins_set):
    """Execute the instruction set <ins_set> and return the last value of the
    accumulator before an infinite loop (or before the normal conclusion of
    the program).  """

    acc = 0
    executed = set()

    i = 0
    while i < len(ins_set):
        if i in executed:
            break

        executed.add(i)

        if ins_set[i][0] == "acc":
            acc += ins_set[i][1]

        i += ins_set[i][1] if ins_set[i][0] == "jmp" else 1

    return acc


def is_halting(ins_set):
    """Execute the instruction set <ins_set> and observe if the program halts.
    If the same instruction is executed twice then the program is deemed to
    be non-halting.  """

    executed = set()

    i = 0
    while i < len(ins_set):
        if i in executed:
            return False

        executed.add(i)

        i += ins_set[i][1] if ins_set[i][0] == "jmp" else 1

    return True


def solve2(ins_set):
    """Naïvely switch JMP to NOP and vice-versa from the instruction set
    <ins_set> and test if the program halts.  """

    # Copy the original instruction set to avoid functional collateral
    # effects.
    ins_copy = ins_set.copy()

    for i, _ in enumerate(ins_set):
        if ins_set[i][0] in ("jmp", "nop"):
            ins_copy[i] = ("nop" if ins_set[i][0] == "jmp" \
                           else "jmp", ins_set[i][1])

            if is_halting(ins_copy):
                break

            ins_copy[i] = ins_set[i]

    return solve1(ins_copy)


# Extract opcode and offset from the instruction.
INS_REG = r"^(\w{3}) ((?:\+?|-)\d+)$"


if __name__ == "__main__":
    usage_and_exit(len(argv) != 2)

    arranged_data = arrange(open_file(argv[1]))
    matched_data = regex(arranged_data, (str, int), INS_REG)

    print(solve1(matched_data))
    print(solve2(matched_data))
