#Swap case
def swap_case(s):
  lis=list(char for char in s)
  for i in range(len(lis)):
      if lis[i].islower():
          lis[i]=lis[i].upper()
      else:
          lis[i]=lis[i].lower()
  return "".join(lis)   
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)