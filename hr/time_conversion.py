#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # check for AM, s[-2:] and 12 s[:2]
    if s[-2:] == "AM" and s[:2] == "12":
        return "00" + s[2:-2]
    # check for AM, s[-2:]
    elif s[-2:] == "AM":
        return s[:-2]    
    # check for PM, s[-2:] and 12 s[:2]
    elif s[-2:] == "PM" and s[:2] == "12":
        return s[:-2]
    # else PM, s[:2] + 12
    else:
        return str(int(s[:2]) + 12) + s[2:8]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()