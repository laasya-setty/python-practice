# Day 6 : Let's Review
n=int(input())

s1=[]
s2=[]
for i in range(n):
    s=input()
    for j in range(0,len(s)):
        if j==0 or j%2==0:
            s1.append(s[j])
        else:
            s2.append(s[j])
    print("".join(s1),"".join(s2))
    s1.clear()
    s2.clear()
        