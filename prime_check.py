n=int(input("enter the number: "))
flag=True
for i in range(3,n):
    if(n%i==0):
        flag=False
        break;
if flag==True:
    print("prime");
elif flag==False:
    print("non-prime");
