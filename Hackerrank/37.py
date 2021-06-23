# Check Strict Superset
#A strict superset has at least one element that does not exist in its subset.
s1=set(map(int,input().split()))
n=int(input())
cnt=0
for i in range(n):
    s2=set(map(int,input().split()))
    if s1.issuperset(s2)==False:
        
        cnt+=1
    else:
        pass
if cnt>0:
    print("False")
else:
    print("True")    