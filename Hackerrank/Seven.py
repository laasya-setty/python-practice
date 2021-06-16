#find the runner up score
n=int(input())
lis=[]
for i in range(n):
    
    lis.append(int(input()))
lis.sort(reverse=True)
print(lis)
for i in range(n):
    if i!=n-1:
        
      if lis[i]==lis[i+1]:
        continue
      else:
        print(lis[i+1])
        break

'''
problem in  above code is it is not taking input in one line (eg: 2 3 4 5 6)
error: invalid literal for int() with base 10: '2 3 6 6 5'
'''

'''
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    res=list(arr)
    res.sort(reverse=True)
    for i in range(len(res)):
        if res[0]!=res[i]:
            temp=i
            break
    print(res[temp])
    '''