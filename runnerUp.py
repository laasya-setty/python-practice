if __name__ == '__main__':
    n = int(input())
    arr = map(int ,input().split())
    res=list(arr)
    res.sort(reverse=True)
    for i in range(len(res)):
        if res[0]!=res[i]:
            temp=i
            break
    print(res[temp])    
        
        
        