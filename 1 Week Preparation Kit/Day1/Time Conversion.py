#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    s = list(s)
    
    ampm = "".join(s[-2:])
    
    if ampm == "PM":
        if "".join(s[:2]) == "12":
            pass
        else:
            tmp = int("".join(s[:2]))
            
            tmp += 12
            tmp1,tmp2 = list(str(tmp))
            s[0],s[1] = tmp1,tmp2
    
    else:
        if "".join(s[:2]) == "12":
            s[0],s[1] = "0","0"
            
 
    return "".join(s[:-2])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
