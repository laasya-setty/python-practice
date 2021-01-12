if __name__ == '__main__':
    N = int(input())
    lis=[]
    for i in range(N):
        inp=input().split() 
        for i in range(1,len(inp)):
           inp[i]=int(inp[i])
        
        if inp[0] == "append":
           lis.append(inp[1])
           
        elif inp[0]=="insert":
            lis.insert(inp[1],inp[2])
        elif inp[0]=="extend":
            lis.extend(inp[1:])
        elif inp[0]=="remove":
            lis.remove(inp[1])
        elif inp[0]=="pop":
            lis.pop()
        elif inp[0]=="index":
            lis.index(inp[1])
        elif inp[0]=="count":
            lis.count(inp[1])
        elif inp[0]=='sort':
            lis.sort()
        elif inp[0]=="reverse": 
            lis.reverse()
        elif inp[0]=="print":
            print(lis)                    
            
   

