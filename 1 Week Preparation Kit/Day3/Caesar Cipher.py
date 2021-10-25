#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
def caesarCipher(s,k):
    
    if k == 0:
        return s
    
    low_alphabet = [chr(i) for i in range(97, 97+26)]
    up_alphabet = [chr(i) for i in range(65, 65+26)]
    
    upper = []
    for w in range(len(s)):
        if s[w] in up_alphabet:
            upper.append(w)
            
    s = s.lower()
    
    for i in range(1,k+1):
        
        i = i%26

        new_f = []

        for word in s:

            if word in low_alphabet:

                if ord(word)+i > (97+25):
                    f = chr(ord(word)+i-26)
                else:
                    f = chr(ord(word)+i)
            else:
                f = word

            new_f.append(f)
            
    for k in range(len(new_f)):
        if k in upper:
            new_f[k] = new_f[k].upper()

    return "".join(new_f)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
