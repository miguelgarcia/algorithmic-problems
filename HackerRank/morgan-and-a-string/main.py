#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the morganAndString function below.
def morganAndString(a, b):
    result = ''
    a += 'z'
    b += 'z'
    i=0
    j=0
    while a[i] != 'z' and b[j] != 'z':
        if a[i:]<b[j:]:
            result += a[i]
            i+=1
        else:
            result += b[j]
            j+=1       
    result = "".join(result) + "".join(a[i:]) + "".join(b[j:])
    result = result.replace('z', '')
    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()
