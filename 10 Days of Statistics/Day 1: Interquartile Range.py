#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    def median(arr):
        if len(arr)%2 == 0:
            mid1, mid2 = len(arr)//2-1, len(arr)//2
            return (arr[mid1]+arr[mid2])/2
        else:
            mid = len(arr)//2
            return arr[mid]

    arr = []
 
    for i in range(len(freqs)):
        for j in range(freqs[i]):
            arr.append(values[i])
    arr.sort()
    
    if len(arr)%2 == 0:
        lower_point = median(arr[:len(arr)//2])
        #print(arr[:len(arr)//2])
        upper_point = median(arr[len(arr)//2:])
        #print(arr[len(arr)//2+1:])
   
    else:
       lower_point = median(arr[:len(arr)//2])
       #print(arr[:len(arr)//2])
       upper_point = median(arr[len(arr)//2+1:])
       #print(arr[len(arr)//2+1:]) 
            
    print(float(upper_point-lower_point))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
