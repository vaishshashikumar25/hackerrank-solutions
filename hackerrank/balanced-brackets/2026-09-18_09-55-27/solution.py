#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    stack = []

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack:
                return "NO"

            top = stack.pop()

            if ch == ')' and top != '(':
                return "NO"
            if ch == ']' and top != '[':
                return "NO"
            if ch == '}' and top != '{':
                return "NO"

    if len(stack) == 0:
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
