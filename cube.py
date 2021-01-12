import math
number=int(input())
brick=[]
c=0
for i in range(number):
    brick.append(list(map(str,input().split())))
for j in range(number):
    for k in range(number):
        if brick[j][k]=='D':
            c+=1

print(math.floor(math.sqrt(c)))