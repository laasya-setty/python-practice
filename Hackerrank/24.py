#The Minion Game
'''
answer correct, but need code optimisation 
'''

def minion_game(string):
    # your code goes here
    kev_v=[]
    stu_c=[]
    cnt_k=0
    cnt_s=0
    k=0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if s[i] in ['a','e','i','o','u','A',"E","I","O","U"]:
                temp=s[i:j]
                if temp in kev_v:
                    cnt_k+=1
                    kev_v.append(s[i:j])
                    
                else:
                    kev_v.append(s[i:j])
                    cnt_k+=1
            else:
                temp=s[i:j]
                if temp in stu_c:
                    cnt_s+=1
                    stu_c.append(s[i:j])
                else:
                    stu_c.append(s[i:j])
                    cnt_s+=1
    if cnt_k>cnt_s:
        print("Kevin",cnt_k )
    elif cnt_k<cnt_s:
        print("Stuart",cnt_s)
    else: 
        print("Draw")        
    
                      
                
            

if __name__ == '__main__':
    s = input()
    minion_game(s)