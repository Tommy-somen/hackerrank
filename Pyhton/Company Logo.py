#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    s = sorted(s)
    
    alphabet = {}
    alphabet[s[0]] = 1
    
    for i in range(1,len(s)):
        if alphabet.get(s[i]) != None:
            alphabet[s[i]] += 1
        else:
            alphabet[s[i]] = 1
    
    ans_box = []
    set_s = list(set(s))
    
    for j in range(len(set_s)):
        ans_box.append([set_s[j],alphabet[set_s[j]]])
        
    ans = sorted(ans_box, key=lambda x:(-x[1],x[0]))
    
    box = []
    for k in range(3):
        box.append([ans[k][0],ans[k][1]])
    
    for l in range(3):
        print(ans[l][0],ans[l][1])
