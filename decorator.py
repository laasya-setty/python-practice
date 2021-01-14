def smart_divide(func):
    def inner(a,b):
        print("Going to divide a and b")
        if(b==0):
           print("Sorry! You are not divisible")
           return
        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    print(a/b)
divide(2,0)

# lines 10 to 13 are equivalent too
""""def divide(a,b):
    print(a/b)
    divide=smart_divide(divide)"""""
    #that parameters of the nested inner() function inside the decorator is the same as the parameters of functions it decorates.
        