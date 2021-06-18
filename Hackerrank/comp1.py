def findShortestSubstring(s):
    # Write your code here
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                x=False
            else :
                x=True
    if x==False:
        return 0
    else:
        lis=[]
        temp=[]
        cnt=0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    temp.append(j)
                    lis.insert(cnt,s[i])
                    cnt+=1
                else:
                    lis.insert(cnt,s[i])
        temp.sort()
        if len(temp)!=0:
            s1=s[0:len(temp)+1]
        for i in range(len(s1)):
            for j in range(i+1,len(s1)):
                if s1[i]==s1[j]:
                    s1.replace(s[j],"")
        return len(s1)-1       
                       
            
            
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = findShortestSubstring(s)

    fptr.write(str(result) + '\n')

    fptr.close()
