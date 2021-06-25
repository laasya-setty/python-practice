# itertools.combinations()
import itertools
n=input().split()
s=n[0]
k=int(n[1])
for i in range(1,k+1):
    for j in itertools.combinations(sorted(s),i):
        print("".join(j))