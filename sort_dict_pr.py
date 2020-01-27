'''sort a dictionary by key or value'''
dict1={}
n=int(input("enter the number of element in dict1: "))
while n>0:
    key=input("enter the key: ")
    value=int(input("enter the value: "))
    dict1.update({key:value})
    n-=1
dict1=sorted(dict1.items(),key=lambda x:x[0])
print(dict1)