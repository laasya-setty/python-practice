#program to check whether a number is prime or not
num=int(input())
def solve():
    
    if num<1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
if solve():
    print("is a prime number")
else:
    print("is not a prime number")    
  