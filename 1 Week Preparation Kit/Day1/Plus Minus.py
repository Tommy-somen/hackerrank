#!/bin/python3

import math
import os
import random
"""
n > 0, n == 0, n < 0の割合を求める。
"""
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive_cnt = 0
    negative_cnt = 0
    zero_cnt = 0
    
    len_arr = len(arr)
    
    for num in arr:
        if num > 0:
            positive_cnt += 1
        elif num < 0:
            negative_cnt += 1
        else:
            zero_cnt += 1
    
    print(positive_cnt/len_arr)
    print(negative_cnt/len_arr)
    print(zero_cnt/len_arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
