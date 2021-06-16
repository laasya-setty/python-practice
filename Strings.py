s="Www.HackerRank.com"
lis=list(char for char in s)
for i in range(len(lis)):
      if lis[i].islower():
          lis[i]=lis[i].upper()
    
print("".join(lis))