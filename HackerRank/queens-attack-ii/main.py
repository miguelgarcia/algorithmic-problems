#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    # Center all cordinates to make the queen be at (0,0)
    obstacles = [[o[0]-r_q,o[1]-c_q] for o in obstacles]
    min_c=1-c_q
    max_c=n-c_q
    min_r=1-r_q
    max_r=n-r_q

    # Add obstacles to prevent the queen from going outside the board
    obstacles.append([0,min_c-1])
    obstacles.append([0,max_c+1])
    obstacles.append([min_r-1, 0])
    obstacles.append([max_r+1, 0])
    #D0 up left
    obstacles.append([-min_c+1,min_c-1])
    obstacles.append([max_r+1,-max_r-1])
    #D1 up right
    obstacles.append([max_c+1,max_c+1])
    obstacles.append([max_r+1,max_r+1])
    #D2 down right
    obstacles.append([-max_c-1,max_c+1])
    obstacles.append([min_r-1,-min_r+1])
    #D3 down left
    obstacles.append([min_c-1,min_c-1])
    obstacles.append([min_r-1,min_r-1])
    
    # Calc coordinate of the closest obstacle in each direction
    left = max([o[1] for o in obstacles if o[0] == 0 and o[1] < 0])
    right = min([o[1] for o in obstacles if o[0] == 0 and o[1] > 0])
    up = min([o[0] for o in obstacles if o[1] == 0 and o[0] > 0])
    down = max([o[0] for o in obstacles if o[1] == 0 and o[0] < 0])
    d0 = min([o[0] for o in obstacles if abs(o[0]) == abs(o[1]) and o[0] > 0 and o[1] < 0])
    d1 = min([o[0] for o in obstacles if abs(o[0]) == abs(o[1]) and o[0] > 0 and o[1] > 0])
    d2 = max([o[0] for o in obstacles if abs(o[0]) == abs(o[1]) and o[0] < 0 and o[1] > 0])
    d3 = max([o[0] for o in obstacles if abs(o[0]) == abs(o[1]) and o[0] < 0 and o[1] < 0])

    # Calculate distance from queen to closes obstacle in each direction
    cells_left = abs(left) - 1
    cells_right = abs(right) -1
    cells_up = abs(up) -1
    cells_down = abs(down) - 1
    cells_d0 = abs(d0) - 1
    cells_d1 = abs(d1) - 1
    cells_d2 = abs(d2) - 1
    cells_d3 = abs(d3) - 1
    return cells_left+cells_right+cells_up+cells_down+cells_d0+cells_d1+cells_d2+cells_d3



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
