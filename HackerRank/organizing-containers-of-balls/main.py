#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    # The only operation is swapping balls
    # So, it's only possible if for every ball type there exists a container
    # with that amount of balls, not used yet for another type.
    balls_by_type = [0] * len(container)
    for c in container:
        for i in range(0, len(c)):
            balls_by_type[i] += c[i]
    containers_quantities = list(map(sum, container))
    balls_by_type.sort()
    containers_quantities.sort()
    if balls_by_type == containers_quantities:
        return "Possible"
    return "Impossible"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
