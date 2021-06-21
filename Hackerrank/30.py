#symmetric differnce
# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
arr = set(map(int, input().split()))
n=int(input())
arr1 =set(map(int, input().split()))

res=sorted(arr.symmetric_difference(arr1))
for i in res:
    print(i)
