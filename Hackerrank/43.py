# Triangle Quest 2
'''n=int(input())
k=1
cnt=0
for i in range(1,n+1):
    for j in range(k):
        
        t=k//2 
        if cnt!=t+1:
            cnt+=1
            print(cnt,end="")
        else:
            print(cnt-1,end='')
            
    print("\r")
    k=k+2
    cnt=0'''

'''
easy approach is it is sq(1),sq(11),sq(111)
'''
for i in range(1,int(input())+1):
    print(((10**i-1)//(9))**2)
   
    