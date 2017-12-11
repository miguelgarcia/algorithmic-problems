import sys

read = sys.stdin.readline

def solve2(mods):
  # L1
  fresh = mods[0]

  # sequences of groups of len 2 with g0+g1%2==0
  # L2
  fresh += int(mods[1] / 2)

  # remainder
  if mods[1] % 2: # one group not in a sequence
    fresh+=1
  return fresh

def solve3(mods):
  #L1
  fresh = mods[0]

  #L2
  seqs_2 = min(mods[1], mods[2]) # sequences of groups of len 2 with g0+g1%3==0
  fresh += seqs_2 # first group on each sequence receives new chocolate
  mods[1] -= seqs_2
  mods[2] -= seqs_2

  #L3
  # now mods[1] == 0 || mods[2] == 0
  if mods[1] > 0:
    fresh += int(mods[1] / 3) # sequences of 3 groups with g%3==1, first of each sequence receives fresh
    mods[1] = mods[1] % 3
  if mods[2] > 0:
    fresh += int(mods[2] / 3) # sequences of 3 groups with g%3==2, first of each sequence receives fresh
    mods[2] = mods[2] % 3

  # remainder
  if mods[1] > 0 or mods[2] > 0:
    # (mods[1] <= 2 and mods[2] == 0) or (mods[1] == 0 and mods[2] <= 2)
    fresh += 1
  return fresh

def solve4(mods):
  #L1
  fresh = mods[0]

  #L2
  fresh += int(mods[2] / 2)
  mods[2] = mods[2] % 2

  seqs_g1_g3 = min(mods[1], mods[3])
  fresh += seqs_g1_g3
  mods[1] -= seqs_g1_g3
  mods[3] -= seqs_g1_g3

  #L3
  # mods[1] == 0 or mods[3] == 0
  if mods[2] == 1:
    if mods[1] >= 2:
      fresh += 1
      mods[1] -= 2
      mods[2] = 0
    if mods[3] >= 2:
      fresh += 1
      mods[3] -= 2
      mods[2] = 0

  #L4
  fresh += int(mods[1] / 4) + int(mods[3] / 4)
  mods[1] = mods[1] % 4
  mods[3] = mods[3] % 4

  # mods2 == 1 and mods1 <2 and mods3<2 and (mods1==0 or mods3==0)
  # or mods2 == 0 and ((mods1 <4 and mods3==0) or (mods1 ==0 and mods3<4))
  #   In any case, only the first remaining group will receive fresh chocolate
  if mods[1] > 0 or mods[2] > 0 or mods[3] > 0:
    fresh += 1
  return fresh

def solve(n, p, groups):
  mods = [0, 0, 0, 0]
  for g in groups:
    mods[g%p] += 1
  if p == 2:
    return solve2(mods)
  if p == 3:
    return solve3(mods)
  if p == 4:
    return solve4(mods)
  return 0

t = int(read())
for caseN in range(1,t+1):
  n,p = map(int, read().split())
  groups = map(int, read().split())
  print("Case #%d: %d" % (caseN, solve(n, p, groups)))