#collections.counter()
import collections
n=int(input())
shoe_size=list(map(int,input().split()[:n]))
m=int(input())
cnt=dict(collections.Counter(shoe_size))
money=0
for i in range(m):
    temp=input().split()
    if int(temp[0]) in cnt.keys():
       if cnt[int(temp[0])]>=1:
          money+=int(temp[1])
          cnt[int(temp[0])]=cnt[int(temp[0])]-1
    else:
        pass
print(money)

        
