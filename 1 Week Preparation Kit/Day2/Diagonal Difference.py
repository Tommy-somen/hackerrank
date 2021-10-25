#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    leftup_to_rightdown = 0
    rightup_to_leftdown = 0
    
    len_arr = len(arr)
    
    for i in range(len_arr):
        leftup_to_rightdown += arr[i][i]
        rightup_to_leftdown += arr[i][-i-1]
        
    return abs(leftup_to_rightdown-rightup_to_leftdown)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
