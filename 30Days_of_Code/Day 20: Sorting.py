#!/bin/python3

import math
import os
import random
import re
import sys

#Write Function
def bubble_sort(arr):
    
    swap_cnt = 0
    swap_flg = True
    limit = len(arr)
    
    while swap_flg == True:
        
        swap_flg = False
        
        for i in range(0,limit-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap_cnt += 1
                swap_flg = True
        
        limit -= 1
    
    print("Array is sorted in",swap_cnt,"swaps.")
    print("First Element:",arr[0])
    print("Last Element:",arr[-1])

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    #Write Here
    bubble_sort(arr)
