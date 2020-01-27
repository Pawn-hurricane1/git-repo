import time
def decor(func):
    def inner(a,b):
        print("you in a decorator now")
        a+=2
        return func(a,b)
    return(inner)

@decor
def func(a=0,b=0):
    # start_time1=time.time()
    c=a+b
    # print(time.time() - start_time1)
    # print(c)

    return(c)




# start_time=time.time()

print(func(3,4))
# print(time.time()-start_time)
