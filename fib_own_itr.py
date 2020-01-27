class Fib_Own_Itr:

    def __init__(self,limit,a=0,b=1,c=2):
        self.limit=limit
        self.a=a
        self.b=b
        self.c=c

    def __iter__(self):
        return self

    def __next__(self):
       if self.c>=self.limit:
           raise StopIteration
       c1 = self.a + self.b
       self.a, self.b = self.b,c1
       self.c += 1
       return(c1)


print("0")
print("1")
f=Fib_Own_Itr(10)

for i in f:
    print(i)