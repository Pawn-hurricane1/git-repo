class Aman:
    def func(self):
        print("aman is a good boy")

    def __call__(self):
        print("callable is called")

a=Aman()
print(callable(Aman))
print(callable(a()))