# Day10 Binary Numbers
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    bina=bin(n)[2:]
    l=list(map(int,bina))
    cnt=0
    temp=[]
    for i in range(len(l)):
        if l[i]==1:
            cnt+=1
            temp.append(cnt)
        else:
            cnt=0
    temp.sort(reverse=True)
    print(temp[0])
        