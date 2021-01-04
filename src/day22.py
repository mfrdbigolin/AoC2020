#!/bin/python3

# Copyright (C) 2021 Matheus Fernandes Bigolin <mfrdrbigolin@disroot.org>
# SPDX-License-Identifier: MIT

"""Day Twenty-Two, Crab Combat."""


from sys import argv
from copy import deepcopy

from utils import open_file, arrange, usage_and_exit


def get_score(deck):
    """Get <deck>'s score."""
    score = 0

    for i, card in enumerate(deck):
        score += card * (len(deck) - i)

    return score


def solve(deck1, deck2, recursive=False):
    """Play a game of Space of Cards with the player's one <deck1> and player's
    two <deck2>; if <recursive>, the recursive variant of the game is used.

    Intuitionally I first tried to use the queue.Queue data structure to
    solve this problem, but, in the second part of the challenge I
    perceived its inability to compute slices; therefore, I switched to
    Python's built-in list.  """

    registry1 = []
    registry2 = []
    player1_has_won = False

    while deck1 and deck2:
        if deck1 in registry1 or deck2 in registry2:
            return (get_score(deck1), True)

        registry1.append(deck1)
        registry2.append(deck2)

        card1 = deck1[0]
        card2 = deck2[0]

        deck1 = deck1[1:]
        deck2 = deck2[1:]

        if len(deck1) >= card1 and len(deck2) >= card2 and recursive:
            sub_deck1 = deepcopy(deck1)[:card1]
            sub_deck2 = deepcopy(deck2)[:card2]

            player1_has_won = solve(sub_deck1, sub_deck2, recursive)[1]
        else:
            player1_has_won = card1 > card2

        if player1_has_won:
            deck1 += [card1, card2]
        else:
            deck2 += [card2, card1]

    return (get_score(deck1) if player1_has_won
            else get_score(deck2), player1_has_won)


if __name__ == "__main__":
    usage_and_exit(len(argv) != 2)

    arranged_data = arrange(open_file(argv[1]), sep="\n\n")
    deck_data = [[int(j) for j in arrange(i)[1:]] for i in arranged_data]

    print(solve(deck_data[0], deck_data[1])[0])
    print(solve(deck_data[0], deck_data[1], True)[0])
