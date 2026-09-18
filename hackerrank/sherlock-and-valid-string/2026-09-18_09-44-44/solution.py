#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    values = list(freq.values())

    count = {}
    for x in values:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1

    if len(count) == 1:
        return "YES"

    if len(count) != 2:
        return "NO"

    f = list(count.keys())

    # One character occurs once
    if f[0] == 1 and count[f[0]] == 1:
        return "YES"

    if f[1] == 1 and count[f[1]] == 1:
        return "YES"

    # One character occurs once more than all others
    if abs(f[0] - f[1]) == 1:
        if count[f[0]] == 1 or count[f[1]] == 1:
            return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
