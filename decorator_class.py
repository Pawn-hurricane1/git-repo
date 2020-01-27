class Decorator:
    def __init__(self,func):
        self.func=func


    def __call__(self,name,age):
        print("you are in decorator class now!!!")
        # self.name=self.name+2
        return self.func(name,age)


@Decorator
def func(name,age):
    print(name,"is",age,"years old")

func("aman",21)
