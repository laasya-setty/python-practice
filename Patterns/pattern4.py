# Simple number triangle
'''
1 
2 2
3 3 3
'''
n=int(input())
num=1
for i in range(1,n+1):
    for j in range(0,i):
        print(num,end=" ")
    num+=1    
    print("\r")