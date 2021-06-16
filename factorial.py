 
def solve(num):
    if(num==0):
        return 1
    else:
        return num*solve(num-1)
a=int(input())
print(solve(a))