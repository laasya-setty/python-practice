#capitalize
s=input()
def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s
           
res=solve(s)
print(res)           
            

        
     
