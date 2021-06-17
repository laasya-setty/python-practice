# reverse pyramid of natural numbers
n=int(input())
num=1
for i in range(1,n+1):
    num=num+i
    t=num
    for j in range(0,i):
        
        t-=1
        print(t,end=" ")

    print("\r")    