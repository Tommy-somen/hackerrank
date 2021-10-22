#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

        
    max_val = -float("inf")
        
    for i in range(4):
            
        for j in range(4):
            tmp = [arr[i+1][j+1]]
            tmp.append(arr[i][j]+arr[i][j+1]+arr[i][j+2])
            tmp.append(arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
    
            if sum(tmp) > max_val:
                max_val = sum(tmp)
            
            tmp = []

    print(max_val)
