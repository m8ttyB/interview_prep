#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # sort array
    a.sort()
    # if len(a) == 1, return element
    if len(a) == 1: return a[0]
    # if first 2 values differ, return 1st value
    elif a[0] != a[1]:
        return a[0]
    # if last 2 values differ, return last value
    elif a[len(a) - 1] != a[len(a) - 2]:
        return a[len(a) - 1]
    else:
        # check surrounding values
        for i in range(1, len(a) - 1):
            # if a[i] is unique, return element
            if a[i] != a[i-1] and a[i] != a[i+1]:
                return a[i]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
