#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    bin_n = list(str(bin(n)))
    bin_n.append("#")
    
    cnt = 0
    max_cnt = 0

    for i in range(len(bin_n)):
        #print(bin_n[i])
        if bin_n[i] == "1":
            cnt += 1
        else:
            if cnt > max_cnt:
                max_cnt = cnt
            cnt = 0

    
    print(max_cnt)     
