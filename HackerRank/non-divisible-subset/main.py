#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    groups = [0] * k
    # Group by mod K
    for n in S:
        groups[n%k] += 1
    result = 0
    # A number from the group mod k = i ONLY "collides" with numbers from the group mod k = k - i
    # Special case: i == k - i only one number from that group can be used
    for i in range(1, int(k / 2)+1):
        if i == k-i:
            result += min(1,groups[i])
        else:
            result += max(groups[i], groups[k-i])
    if groups[0] >= 1:
        # Only one number from the group mod k = 0 can be used
        result +=1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)

    fptr.write(str(result) + '\n')

    fptr.close()
