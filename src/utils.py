#!/bin/python3

# Copyright (C) 2020 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""General utilities."""


# Avoid ambiguous namespace with the built-in exit and compile.
from sys import exit as finish
from re import compile as regex_comp
from functools import reduce


def open_file(fname):
    """Open <fname> and return its contents."""
    with open(fname, "r") as reader:
        data = reader.read()

    return data


def arrange(values, dtype=str, sep="\n"):
    """Separate list <values> according to the separator <sep> and return a
    list of <dtype>s.  """

    return [dtype(v) for v in values.split(sep) if v != ""]


def usage_and_exit(is_exit):
    """If <is_exit>, print usage and exit."""
    if is_exit:
        print("usage: ./dayN INPUT")

        finish(1)


def regex(values, dtypes, form):
    """Organize a array of <values> according to a <form> regular
    expression string, return a tuple with the matched with the types
    <dtypes>.  """

    # Typify a tuple of values <ts> according to a tuple of types <dtypes>.
    transfig = \
        lambda ts, dtypes: tuple(dtypes[i](t) for (i, t) in enumerate(ts))

    reg = regex_comp(form)
    matched = [transfig(reg.findall(l)[0], dtypes) for l in values]

    return matched


def product(arr):
    """Return the product of a sequence of elements of <arr>."""
    return reduce(lambda a,b: a*b, arr)
