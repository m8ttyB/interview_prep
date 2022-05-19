#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # create key:val pairs to capture counts
    counts = {1:0,-1:0, 0:0}
    
    for i in arr:
        if i < 0: counts[-1] = counts[-1] +1
        elif i == 0: counts[0] = counts[0] + 1
        elif i > 0: counts[1] = counts[1] + 1

    # iterate over dict and calculate ratios
    for value in counts.values():
        ratio = round(value/len(arr), 6)
        print('%.6f' % ratio)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

    # STDIN -4 3 -9 0 4 1
    # Expected out
    # 0.500000
    # 0.333333
    # 0.166667

    