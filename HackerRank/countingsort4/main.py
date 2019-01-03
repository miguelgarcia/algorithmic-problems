#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    strings_by_x = [ [] for _ in range(100)]
    result = ""
    i = 0
    for v in arr:
        x, s = int(v[0]), v[1]
        strings_by_x[x].append(s if i >= len(arr)/2 else '-')
        i += 1
    for strs in strings_by_x:
        for s in strs:
            if result != "":
                result += " "
            result += s
    return result





if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    print(countSort(arr), end="")
