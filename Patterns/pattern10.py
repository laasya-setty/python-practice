n=int(input())
t=n+n
for i in range(n,0,-1):
    print(' '*(t-i) + '* '*(i))