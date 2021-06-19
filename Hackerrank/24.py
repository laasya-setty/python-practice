#The Minion Game
'''
answer correct, but need code optimisation 


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

'''
'''
Not optimised yet


def minion_game(string):
    # your code goes here
    
    cnt_k=0
    cnt_s=0
    for i in range(len(s)):
        if s[i] in ['a','e','i','o','u','A',"E","I","O","U"]:
            for j in range(i+1,len(s)+1):
                temp=s[i:j] 
                cnt_k+=1
        else:
            for j in range(i+1,len(s)+1):
                temp=s[i:j]
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
    '''
    # The Minion Game in Python - Hacker Rank Solution
def minion_game(string):
    # your code goes here
    # The Minion Game in Python - Hacker Rank Solution START
    player1 = 0;
    player2 = 0;
    str_len = len(string)
    for i in range(str_len):
        if s[i] in "AEIOU":
            player1 += (str_len)-i
        else :
            player2 += (str_len)-i
    
    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart",player2)
    elif player1 == player2:
        print("Draw")
    else :
        print("Draw")
    # The Minion Game in Python - Hacker Rank Solution END

if __name__ == '__main__':
    s = input()
    minion_game(s)