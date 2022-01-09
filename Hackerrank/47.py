# Day 11 2D arrays
arr=[]
maxi=-100000
for i in range(6):
     arr.append(input().split())

for i in range(6):
    for j in range(6):
        arr[i][j]=int(arr[i][j])
print(type(arr[1][0]))
     
     
for i in range(4):
    for j in range(4):
        temp=0
        #top row
        temp+= arr[i][j];
        temp+= arr[i][j+1];
        temp+= arr[i][j+2];
        #middle 
        temp+= arr[i+1][j+1];
        #bottom row
        temp+= arr[i+2][j];
        temp+= arr[i+2][j+1];
        temp+= arr[i+2][j+2];
        if temp>maxi:
            maxi=temp
print(maxi)
    
        
        
        
