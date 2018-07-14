#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    t = [int(x, 2) for x in topic] # binary string to ints
    maxt = -1
    n = 0
    for i in range(0, len(t)):
        for j in range(i+1, len(t)):
            subjects = bin(t[i] | t[j]).count("1") # count subjects
            if subjects > maxt:
                maxt = subjects
                n = 1
            elif subjects == maxt:
                n += 1
    return [maxt, n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
