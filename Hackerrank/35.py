# The Captain's Room
import collections
n=int(input())
s=list(map(int,input().split()))
d=dict(collections.Counter(s))
key=list(d.keys())
val=list(d.values())
p=val.index(1)
print(key[p])