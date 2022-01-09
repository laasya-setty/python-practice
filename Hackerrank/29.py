#set union operation
n=int(input())
s1=set(map(int,input().split()[:n]))
print(s1)
m=int(input())
s2=set(map(int,input().split()[:m]))
s3=s1.union(s2)
print(len(s3))