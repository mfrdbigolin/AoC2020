#!/bin/python3

# Copyright (C) 2020 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""General utilities."""


# Avoid ambiguous namespace with the built-in exit.
from sys import exit as finish


def open_file(fname):
    """Open <fname> and return its contents."""
    with open(fname, "r") as reader:
        data = reader.read()

    return data


def arrange(values, dtype=str, sep="\n"):
    """Separate list <values> according to separator <sep> and return a
    list of <dtype>s.  """

    return [dtype(v) for v in values.split(sep) if v != ""]


def usage_and_exit(is_exit):
    """If <is_exit>, print usage and exit."""
    if is_exit:
        print("usage: ./dayN INPUT")

        finish(1)
