#!/bin/python3

import math
import os
import random
import re
import sys

def rotate(a, n):
    for _ in range(0, n):
        tmp = a[0]
        a = a[1:] + [tmp]
    return a


def matrix_to_squares(matrix, m, n):
    squares = []
    for sq in range(0, int(min(m, n)/2)):
        s = []
        for j in range(sq, n-sq):
            s.append(matrix[sq][j])
        for i in range(sq+1, m-sq-1):
            s.append(matrix[i][n-sq-1])
        for j in range(n-sq-1, sq-1, -1):
            s.append(matrix[m-sq-1][j])
        for i in range(m-sq-2, sq, -1):
            s.append(matrix[i][sq])

        squares.append(s)
    return squares

def squares_to_matrix(squares, m, n):
    matrix = []
    for _ in range(0, m):
        matrix.append([0]*n)
    for sq in range(0, int(min(m, n)/2)):
        s = squares[sq]
        s.reverse()
        for j in range(sq, n-sq):
            matrix[sq][j] = s.pop()
        for i in range(sq+1, m-sq-1):
            matrix[i][n-sq-1] = s.pop()
        for j in range(n-sq-1, sq-1, -1):
            matrix[m-sq-1][j] = s.pop()
        for i in range(m-sq-2, sq, -1):
            matrix[i][sq] = s.pop()
    return matrix



# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    # Make a list with the elements of each inner square
    m = len(matrix)
    n = len(matrix[0])
    squares = matrix_to_squares(matrix, m, n)
    # Rotate left the list of the elements of each square
    # rotate r % len(square) to avoid cycles
    rotated_squares = []
    for s in squares:
        rotated_squares.append(rotate(s, r%len(s)))
    # Rebuild matrix
    rotated = squares_to_matrix(rotated_squares, m ,n)
    for row in rotated:
        print(" ".join(map(str, row)))



if __name__ == '__main__':
    mnr = input().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
