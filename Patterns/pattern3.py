# inverted right triangle
'''
1 1 1 1 1 
2 2 2 2
3 3 3
4 4
5
'''
n=int(input())
num=1
for i in range(n+1):
    for j in range(n-i,0,-1):
        print(num,end=" ")
    num+=1
    print("\r")
