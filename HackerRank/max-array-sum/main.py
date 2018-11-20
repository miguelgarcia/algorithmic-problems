#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    sol_0_max = 0
    sol_0_i = -2
    sol_1_max = 0
    sol_1_i = -2
    for i in range(0,len(arr)):
        new_sol_1_max = sol_1_max
        new_sol_1_i = sol_1_i
        if arr[i] > 0:
            if sol_1_i == i - 1:
                if sol_0_max+arr[i]>sol_1_max:
                    new_sol_1_max = sol_0_max + arr[i]
                    new_sol_1_i = i
            else:
                new_sol_1_max = sol_1_max + arr[i]
                new_sol_1_i = i
        sol_0_max = sol_1_max
        sol_0_i = sol_1_i
        sol_1_max = new_sol_1_max
        sol_1_i = new_sol_1_i
    return sol_1_max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
