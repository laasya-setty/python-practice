# reverse pyramid of numbers
'''
1 
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''
n=int(input())
for i in range(1,n+1):
    t=i
    for j in range(0,i):
        print(t,end=" ")
        t=t-1
    print("\r")