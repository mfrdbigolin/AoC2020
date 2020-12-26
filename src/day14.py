#!/bin/python3

# Copyright (C) 2020 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""Day Fourteen, Docking Data."""


from sys import argv
from re import sub, findall

from utils import open_file, arrange, usage_and_exit, regex, fill


def masker(mask, val):
    """Enforce the defined bits in the <mask> on <val>.  """

    ones = sub(r"[^1]", "0", mask)
    val |= int(ones,2)
    zeros = sub(r"[^0]", "1", mask)
    val &= int(zeros,2)

    return val


# Get the mask value.
MASK_REG = r"^mask = (\w{36})$"
# Get the memory index and value.
MEM_REG = r"^mem\[(\d+)\] = (\d+)$"


def solve(prog, quantic = False):
    """Read the <prog>ram memory instructions and realize the necessary bit
    maskings in the cells of the memory.

    If <quantic>, treat the "X"s as floating ("quantic") bits, meaning that
    the bits can assume every possible permutation.  """

    mask = "0"*36
    mem = {}

    for ins in prog:
        cmd = findall(r"^(\w+)", ins)[0]

        if cmd == "mask":
            mask = findall(MASK_REG, ins)[0]
        elif cmd == "mem":
            idx, val = regex([ins], (int, int), MEM_REG)[0]

            if not quantic:
                mem[idx] = masker(mask, val)
            else:
                idx |= int(sub(r"[^1]", "0", mask), 2)

                # Intermediary mold.
                mold = sub(r"[^X]", "~", mask)

                # Count through every binary permutation of <n_bits>.
                for i in range(2**(n_bits := mold.count("X"))):
                    count = bin(i)[2:].rjust(n_bits, "0")
                    # Fill the "X"s with each bit from the <count>.
                    filled = "".join(fill(mold, "X", count))

                    mem[masker(filled, idx)] = val

    return sum(mem.values())


if __name__ == "__main__":
    usage_and_exit(len(argv) != 2)

    input_data = arrange(open_file(argv[1]))

    print(solve(input_data))
    print(solve(input_data, True))
