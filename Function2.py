# function can return another function
def meth():
    def meth1():
        print("Hai Laasya!")
    return meth1
res=meth()    
res()