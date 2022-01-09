import itertools
n=input()
l=itertools.groupby(n)
for k,v in l:
    print((len(list(v)),int(k)),end=" ")           
            
        

