#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    a = list(a)
    a.append('$')
    b = b +'$'
    lb = len(b)

    prefixes = ['']
    prefixes_dict = {'':True}
    for ch in a:
        if ch.islower():
            for i in range(len(prefixes)):
                if lb > len(prefixes[i]) and b[len(prefixes[i])] == ch.upper():
                    prefix = prefixes[i]+ch.upper()
                    if prefix not in prefixes_dict:
                        prefixes.append(prefix)
                        prefixes_dict[prefix] = True
        else:
            new_prefixes = []
            prefixes_dict = {}
            for p in prefixes:
                if lb > len(p) and b[len(p)] == ch.upper():
                    prefix = p+ch.upper()
                    new_prefixes.append(prefix)
                    prefixes_dict[prefix] = True
            prefixes = new_prefixes

    return "YES" if b in prefixes else "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
