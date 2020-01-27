def fib_gen(limit):
    a=0
    b=1
    counter=2
    while counter<limit:
        yield a+b
        a,b=b,a+b
        counter+=1

f=fib_gen(10)
# # print((f).__next__())
print("0")
print("1")
# for i in f:
#     print(i)
for i in range(8):
    print(f.__next__())