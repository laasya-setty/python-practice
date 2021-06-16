class Quadratic:
    def solve(self,a,b,c):
        bsquare= b*b
        d=4*a*c
        if(bsquare<d):
            print("The roots are complex")  
        elif(bsquare>d): 
            print("The roots are real") 
        else:
            print("The roots are equal") 
obj=Quadratic()
obj.solve(1,-2,1)
    