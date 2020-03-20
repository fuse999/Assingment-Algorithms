#!/usr/bin/python

import sys


def rock_paper_scissors(n):
  possible_plays = [["rock"], ["paper"], ["scissors"]]
  # return empty list if n is zero
  if n == 0:
    return [[]]
  # return possible_plays if n is one
  if n == 1:
    return possible_plays

  multi_plays = []
  rounds = rock_paper_scissors(n - 1)
  # for loop for if n is > 1
  for round in rounds:

     for play in possible_plays:

       new_play = round + play
       multi_plays.append(new_play)

  return multi_plays


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')