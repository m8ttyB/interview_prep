#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # sort int array, low to high
    arr.sort()
    low = sum(arr[:-1])
    high = sum(arr[1:])
    print("%s %s" % (low, high))
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

    # STDIN 1 2 3 4 5
    # Expected Out
    # 10 14