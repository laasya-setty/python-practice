class Score:
    def __init__(self,name,score):
        self.name=name
        self.score=score
        # instance method
    def fun(self):
        print(f"{self.name} scored {self.score} in Mathematics")   
obj=Score("Laasya",99)
obj.fun()     
    