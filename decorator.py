def add1(a, b):
    return a + b


def func2(add1):
    def innerf(a,b):
        print("this function subtract also")
        c=a-b
        #print(c)
        return add1(a,b)
    return innerf


ans=func2(add1)
print(ans(5,3))