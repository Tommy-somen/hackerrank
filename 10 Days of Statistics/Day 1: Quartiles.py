#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    
    arr.sort()
    
    def median(arr):
        if len(arr)%2 == 0:
            mid1, mid2 = len(arr)//2-1, len(arr)//2
            return (arr[mid1]+arr[mid2])/2
        else:
            mid = len(arr)//2
            return arr[mid]
    
    Med = median(arr)
    
    if len(arr)%2 == 0:
        a_fourth = median(arr[:len(arr)//2])
        #print(arr[:len(arr)//2])
        three_fourth = median(arr[len(arr)//2:])
        #print(arr[len(arr)//2+1:])
   
    else:
       a_fourth = median(arr[:len(arr)//2])
       #print(arr[:len(arr)//2])
       three_fourth = median(arr[len(arr)//2+1:])
       #print(arr[len(arr)//2+1:])
    
    return [math.ceil(a_fourth), math.ceil(Med), math.ceil(three_fourth)]

    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
