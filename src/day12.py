#!/bin/python3

# Copyright (C) 2020 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""Day Twelve, Rain Risk."""


from sys import argv
from math import pi, sin, cos

from utils import open_file, arrange, usage_and_exit, regex


# The cardinal points (east, west, north, south).
DIR = "EWNS"


# Scale direction <d> according to offset <o>.
scale = lambda d, o: (-1)**DIR.index(d)*o
# Degrees <d> to radians.
deg_rad = lambda d: ((d*pi)/180) % (2*pi)
# Rotate a vector <v> according to an angle <a>.
rot = lambda v, a: [v[0]*int(cos(a)) - v[1]*int(sin(a)),
                    v[0]*int(sin(a)) + v[1]*int(cos(a))]


def solve(actions, way = None, anchor = True):
    """Return the ship's Manhattan distance after performing a series of
    <actions>; the actions are relative to a waypoint <way> vector, which
    itself is relative to the ship's position.  If <way> is <anchor>ed,
    then its length is fixed.

    The default value for <way> is the vector [1,0], i.e., the cardinal
    east.  """

    if way is None:
        way = [1,0]
    ship = [0,0]

    for (act, off) in actions:
        if act in DIR:
            if anchor:
                ship[DIR.index(act) // 2] += scale(act, off)
            else:
                way[DIR.index(act) // 2] += scale(act, off)

        if act == "F":
            ship = [ship[0] + off*way[0], ship[1] + off*way[1]]

        if act in "RL":
            ang = deg_rad(off) if act == "L" else -deg_rad(off)
            way = rot(way, ang)

    return abs(ship[0]) + abs(ship[1])


# Separate actions from offsets.
ACTION_REG = r"(\w{1})(\d+)"


if __name__ == "__main__":
    usage_and_exit(len(argv) != 2)

    input_data = regex(arrange(open_file(argv[1])), (str, int), ACTION_REG)

    print(solve(input_data))
    print(solve(input_data, [10,1], False))
