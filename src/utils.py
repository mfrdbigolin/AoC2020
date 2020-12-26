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


def assoc(soc, preds):
    """Map the predicates contained in dictionary <preds> to the
    values contained in dictionary <soc> and return tautology if all
    associations are truthful.  """

    return all([preds.get(k)(soc.get(k)) for k in soc.keys() \
                if preds.get(k) is not None])


def mod_inv(div, modulo):
    """Return the modular inverse k, such that <div>⋅k≡1(mod <modulo>),
    i.e., k≡<div>⁻¹ (mod <modulo>).  This function uses the Extended
    Euclidean Algorithm.  """

    carry = [0, 1]
    carrier = [div, modulo]

    while carrier[0] != 0:
        quot = carrier[1]//carrier[0]
        carry = [carry[1], carry[0] - quot * carry[1]]
        carrier = [carrier[1] % carrier[0], carrier[0]]

    # Use the modulo operator again to keep only positive numbers.
    return carry[0] % modulo


def fill(lst, mold, subs):
    """For every <mold> element in <lst>, substitute for the according
    <subs> value (indexically).  """

    nlst = list(lst).copy()

    j = 0
    for i, elem in enumerate(lst):
        if elem == mold:
            nlst[i] = subs[j]
            j += 1

    return nlst
