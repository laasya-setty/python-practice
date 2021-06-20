# Merge the tools
from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    num_sub=len(string)/k
    lis=[]
    for i in range(0,len(string),k):
        temp=string[i:i+k]
        lis.append(temp)
    print(lis)
    for i in lis:
        tem=OrderedDict.fromkeys(i)
        i="".join(tem)
        print(i)
        
    
        
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)