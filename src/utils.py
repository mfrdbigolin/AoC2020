#!/bin/python3

# Copyright (C) 2020, 2021 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""General utilities."""


# Avoid ambiguous namespace with the built-in exit and compile.
from sys import exit as finish
from re import findall
from functools import reduce
from collections import Counter


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


# Typify a tuple of values <ts> according to a tuple of types <dtypes>.
transfig = \
    lambda ts, dtypes: tuple(dtypes[i](t) for (i, t) in enumerate(ts))


# Typify a array of tuples <ts> according to a tuple of types <dtypes>.
transfiged = lambda ts, dtypes: [transfig(t, dtypes) for t in ts]


def regex(values, dtypes, form):
    """Organize a array of <values> according to a <form> regular
    expression string, return a tuple with the matched with the types
    <dtypes>.  """

    return [transfig(findall(form, l)[0], dtypes) for l in values]


def product(arr):
    """Return the product of a sequence of elements of <arr>."""

    return reduce(lambda a,b: a*b, arr)


def assoc(soc, preds):
    """Map the predicates contained in dictionary <preds> to the
    values contained in dictionary <soc> and return tautology if all
    associations are truthful.  """

    return all([preds.get(k)(soc.get(k)) for k in soc.keys() \
                if preds.get(k) is not None])


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


# Transform elements from array <ds> into a dictionary, with its head as
# its key and the tail as its values.
dictf = lambda ds: dict(zip([ds[0]], [ds[1:]] if ds[1:] != [] else []))


# Cumulatively merge alike elements from <d>.
merge = lambda d: reduce(lambda a, b: a | b, d)


# Calculate the pairwise difference between elements of a list <lst>.
diff = lambda lst: [pair[0] - pair[1] for pair in zip(lst[1:], lst[:-1])]


def frequency(lst):
    """Return a Counter with the frequency of the elements in <lst>."""
    freq = Counter()

    for elem in lst:
        freq[elem] += 1

    return freq


# Frequency with depth two.
freqd2 = lambda s: reduce(lambda a,b: a + b, [frequency(i) for i in s])
