
from itertools import product
def even(n):
    check_sum=0
    for i in range(len(n)):
        check_sum=check_sum+int(n[i])
    return check_sum
l,h=map(int,input().split())
k=int(input())
lst=[]
for i in range(l,h+1):
    lst.append(str(i))
count_permutations=0
permutation=product(lst,repeat=k)
for i in permutation:
    if (even(i)%2==0):
        count_permutations+=1
print(count_permutations%1000000007)

