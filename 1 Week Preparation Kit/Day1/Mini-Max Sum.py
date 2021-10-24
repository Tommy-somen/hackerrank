#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min_val = float("inf")
    max_val = 0
    
    for v in itertools.combinations(arr,len(arr)-1):
        
        if sum(v) > max_val:
            max_val = sum(v)
        
        if min_val > sum(v):
            min_val = sum(v)
            
    print(min_val, max_val)
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
