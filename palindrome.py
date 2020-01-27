'''checks whether a string is palindrome or not'''
str=input("enter the string: ")
start=0
end=len(str)-1
flag=0
while start<end:
    if str[start]!=str[end]:
        flag=1
        break
    start+=1
    end-=1

if flag==0:
    print("string is palindrome")
else:
    print("string is not a palindrome")
