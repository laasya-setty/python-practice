# function can be passed as an argument in another function
def inc(x):
        print( x+1)
def dec(x):
        return x-1
def operate(func,x):
        res=func(x)
        return res
operate(inc,4)     
