# Check Subset
n=int(input())
temp=[]
for i in range(n):
    m1=int(input())
    s1=set(map(int,input().split()[:m1]))
    m2=int(input())
    s2=set(map(int,input().split()[:m2]))
    temp.append(s1.issubset(s2))
for i in temp:
    print(i)
    
    