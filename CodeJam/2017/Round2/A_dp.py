# Solution using dynamic programming

import sys
import numpy as np

read = sys.stdin.readline
MAX_GROUPS = 100

# memoization area
# memo[L][a][b][c] = solve_dp(...,L,[a,b,c])
memo = np.zeros((4, MAX_GROUPS, MAX_GROUPS , MAX_GROUPS), np.int)

#
# How many groups receive fresh bars if there are L old pieces
# to be consumed and 
#
# available[0] Number of groups with a number of members mod p == 1
# available[1] Number of groups with a number of members mod p == 2
# available[2] Number of groups with a number of members mod p == 3
#
def solve_dp(p, L, available):
  if memo[L][available[0]][available[1]][available[2]] != 0:
    return memo[L][available[0]][available[1]][available[2]]
  if sum(available) == 0:
    return 0
  best = 0
  for i in range(0, len(available)):
    if available[i] > 0:
      available[i] = available[i] - 1
      tmp = solve_dp(p, (L+i+1) % p, available)
      available[i] = available[i] + 1
      best=max(best,tmp)  
  if L == 0:
    best += 1
  memo[L][available[0]][available[1]][available[2]] = best
  return best
      
def solve(n, p, groups):
  memo.fill(0)
  # partition the groups based on the mod p
  mods = np.zeros(4, np.int)
  for g in groups:
    mods[g%p] += 1
  # groups with a number of members divisible by p can be cosnumed greedy
  # and doest no affect the ordering of the rest of the groups
  fresh = mods[0]
  fresh += solve_dp(p, 0, mods[1:])
  return fresh
  

t = int(read())
for caseN in range(1,t+1):
  n,p = map(int, read().split())
  groups = map(int, read().split())
  print("Case #%d: %d" % (caseN, solve(n, p, groups)))
