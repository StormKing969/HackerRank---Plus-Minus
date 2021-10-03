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
    total = len(arr)
    pos = 0
    neg = 0
    zero = 0
    
    for i in range(total):
        if arr[i] > 0:
            pos += 1
        if arr[i] < 0:
            neg += 1
        if arr[i] == 0:
            zero += 1
    
    posRatio = pos/total
    negRatio = neg/total
    zeroRatio = zero/total
    
    print("{:.6f}".format(posRatio));
    print("{:.6f}".format(negRatio));
    print("{:.6f}".format(zeroRatio));

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
