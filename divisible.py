'''program checks whether the number is divisible by sum of its digits or not'''

def isdiv(num):
    sum=0
    for i in num:
        sum+=int(i)
    if int(num)%sum==0:
        return True
    else:
        return False
it=int(input("enter the number of iterations: "))
while it>0:
    num=input("enter the number: ")
    print(isdiv(num))
    it-=1
