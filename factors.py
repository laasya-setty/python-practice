# finding factors of a given number
num=int(input())
for i in range(1,num+1):
    if(num%i==0):
        print(i,"is a factor")