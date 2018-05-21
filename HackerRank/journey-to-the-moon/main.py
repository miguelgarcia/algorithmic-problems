#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the journeyToMoon function below.
def journeyToMoon(n, astronaut):
    # A) Make lists of astronauts by countries
    #    Only include countries with more than one astronaut, a pair of
    #    astronauts exists in `astronaut`
    astronauts_by_country = []
    for pair in astronaut:
        c_a = None
        c_b = None
        for i in range(0, len(astronauts_by_country)):
            if pair[0] in astronauts_by_country[i]:
                c_a = i
            if pair[1] in astronauts_by_country[i]:
                c_b = i
            if c_a is not None and c_b is not None:
                break
        if c_a is None and c_b is None:
            astronauts_by_country.append(pair)
        elif c_a is None:
            astronauts_by_country[c_b].append(pair[0])
        elif c_b is None:
            astronauts_by_country[c_a].append(pair[1])
        elif c_a != c_b:
            astronauts_by_country[c_a].extend(astronauts_by_country[c_b])
            astronauts_by_country[c_b] = []
    # Calculate the count by country     
    n_by_country = list(map(len, astronauts_by_country))
    result = 0
    # Each astronaut of a country can travel with each astronaut of the rest
    # of the countries
    for i in range(0, len(n_by_country)):
        for j in range(i+1, len(n_by_country)):
            result += n_by_country[i] * n_by_country[j]
    
    # Finally consider astronauts not belonging to a country with two or more
    # astronauts
    lonely_astronauts = n - sum(n_by_country)
    # Can travel with every astronaut belonging to a country with two or more
    result += lonely_astronauts * sum(n_by_country)
    # Calculate the combinations of astronauts from countries with only one astronaut
    # comb(lonely_astronauts, 2)
    if lonely_astronauts > 1:
        result += lonely_astronauts*(lonely_astronauts-1) / 2.
    return int(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
