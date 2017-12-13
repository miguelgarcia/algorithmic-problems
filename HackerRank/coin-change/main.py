#!/bin/python3
# https://www.hackerrank.com/challenges/coin-change/problem
#
# numpy not enabled in this problem !

import sys
#import numpy

MAX_AMOUNT = 250
MAX_COINS = 50
memo = None

# How many different ways of making amount with any combination of coins
# with index in the list of coins >= min_coin_index exist
#
# the min_coin_idx constraint is needed to avoid counting repetitions:
# ex 75 = 50 + 25 and 25 + 50 but the order is not important, they are both the
# same solution, thus, must be counted only once
#
def solve(amount, coins, min_coin_idx):
  if amount == 0:
    return 1
  if amount < 0:
    return 0
  #if memo[amount][min_coin_idx] > 0:
  if amount not in memo:
    memo[amount] = dict()
  elif min_coin_idx in memo[amount]:
    return memo[amount][min_coin_idx]
  solutions = 0
  for coin_idx in range(min_coin_idx, len(coins)):
    solutions += solve(amount-coins[coin_idx], coins, coin_idx)
  memo[amount][min_coin_idx] = solutions
  return solutions


def getWays(n, c):
    # Complete this function
    globals()["memo"] = dict() #numpy.zeros([MAX_AMOUNT, MAX_COINS], numpy.int)
    print(solve(n, c, 0))

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
