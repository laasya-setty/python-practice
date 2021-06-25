#Day 8 : Dictionaries
n=int(input())
d={}
for i in range(n):
    temp=input().split()
    d[temp[0]]=int(temp[-1])
while True:
    try: 
       name=input()
       if name in d:
          print(name,"=",d[name],sep='')
       else:
          print("Not found")
    except:
        break
