#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    #Not using reverse() function
    length = len(arr)
    
    mid = length//2

    for i in range(mid):
        arr[i], arr[-i-1] = arr[-i-1], arr[i]  
    
    print(*arr)
