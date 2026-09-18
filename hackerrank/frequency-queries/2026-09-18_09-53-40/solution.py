#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    values = {}
    frequencies = {}

    result = []

    for query in queries:
        operation = query[0]
        value = query[1]

        if operation == 1:
            old = values.get(value, 0)
            values[value] = old + 1

            if old > 0:
                frequencies[old] -= 1

            frequencies[old + 1] = frequencies.get(old + 1, 0) + 1

        elif operation == 2:
            if value in values and values[value] > 0:
                old = values[value]
                values[value] -= 1

                frequencies[old] -= 1
                frequencies[old - 1] = frequencies.get(old - 1, 0) + 1

        elif operation == 3:
            if frequencies.get(value, 0) > 0:
                result.append(1)
            else:
                result.append(0)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
