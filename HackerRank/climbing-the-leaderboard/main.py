#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    result = []
    rank = 1
    prev_score = -1
    for s in scores:
        if len(alice) == 0:
            break
        if s == prev_score:
            continue
        
        prev_alice=-1
        while len(alice) > 0 and alice[-1] >= s:
            result.append(rank)
            prev_alice=alice.pop()
        rank += 1
        prev_score = s
    for a in alice:
        result.append(rank)
    return reversed(result)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
