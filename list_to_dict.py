#input("enter the list whose dictionary is to be made: ")
'''program converts a list into dictionary'''
list1 = list(input("enter the members of a list: ").split())
print(list1)
dict1 = {}
# print(dict1)
for letter in list1:
    #print(list1.count(letter))
    if letter not in dict1:
        # print(letter)
        dict1.update({letter:list1.count(letter)})
        #dict1[letter]=list1.count(letter)

print(dict1)
