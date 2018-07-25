#!/bin/python3

import math
import os
import random
import re
import sys

def show(grid):
    tmp = ["".join(row) for row in grid]
    print('\n'.join(tmp))
    print('\n')

# Complete the bomberMan function below.
def bomberMan(n, grid):
    memo = dict()
    if n == 1:
        return grid
    grid = [list(row) for row in grid]
    s = 2
    cycle = None
    its=0
    while s <= n:
        its+=1
        if s % 2 == 0:
            # plant and increment planted timer
            grid = [['1' if x == 'O' else 'O' for x in row] for row in grid]
        else:
            # boom
            for i in range(0, len(grid)):
                for j in range(0, len(grid[0])):
                    if grid[i][j] == 'O':
                        for y in range(-1,2):
                            if i+y >= 0 and i+y<len(grid) and grid[i+y][j] == '1':
                                grid[i][j] = '.'
                        for x in range(-1,2):
                            if j+x>=0 and j+x<len(grid[0]) and grid[i][j+x] == '1':
                                grid[i][j] = '.'
            grid = [['.' if x == '1' else x for x in row] for row in grid]

        # Detect cycles to avoid computations
        key = "".join(["".join(row) for row in grid])
        if key not in memo:
            memo[key] = s
        elif cycle is None:
            cycle = s-memo[key]
            s = s + cycle * int((n-s) / cycle)
        s+=1
    return ["".join(row).replace('1', 'O') for row in grid]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
