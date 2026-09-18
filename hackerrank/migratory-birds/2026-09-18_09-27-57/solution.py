#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    d = {}

    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    maximum = 0
    key = 0

    for i in d:
        if d[i] > maximum:
            maximum = d[i]
            key = i

        elif d[i] == maximum and i < key:
            key = i

    return key
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
