#set mutations
n=int(input())
s1=set(map(int,input().split()[:n]))
m=int(input())
for i in range(m):
    inp=input().split()
    s2=set(map(int,input().split()[:int(inp[1])]))
    if inp[0]=="intersection_update":
        s1.intersection_update(s2)
    elif inp[0]=="update":
        s1.update(s2)
    elif inp[0]=="symmetric_difference_update":
        s1.symmetric_difference_update(s2)
    else:
        s1.difference_update(s2)
print(sum(s1))