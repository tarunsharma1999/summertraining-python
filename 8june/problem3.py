list_elements =input("Enter elements of list")
list= list_elements.split()
print("number greater than 5:")

l=[list[num] for num in range (len(list)) if int(list[num]) >5 ]
print (l)

print("number less than or equal to 2:")

l2=[list[num] for num in range (len(list)) if int(list[num]) <=2]
print(l2)

