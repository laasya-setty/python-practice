#Nested Lists
n=int(input())
lis=[]


for i in range(n):
    name=input()
    score=float(input())
    lis.append([name,score])
    
lis.sort(key= lambda x:x[1] )  #sorting in nested lists
high=sorted(set([score for name, score in lis]))[1]
print(high)
print('\n'.join(sorted([name for name, score in lis if score ==high])))


## below is trying to write in normal version
# instead of list comprehension
# errors are there
s=[]
for score , name in lis:
    s.append(score)
s=set(s)
s=sorted(s)
high=s[1][1]
print(high)
for score, name in lis:
    if score==high:
        print(name)

    



