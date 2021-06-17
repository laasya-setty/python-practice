# pyramid of natural numbers
'''
1 
2 3
4 5 6
'''
n=int(input())
num=0
for i in range(1,n+1):
    for j in range(0,i):
        num=num+1
        print(num,end=" ")
    print("\r")    