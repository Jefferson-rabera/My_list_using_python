# create an empty list called my list
my_list = []
# add the numbers 1, 2, and 3 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# print after appending the contents of my_list
print("Contents of my_list after appending:", my_list)

#insert 15 after the second positoin
my_list.insert(2, 15)

#extend with [50, 60, 70   ]
my_list.extend([50, 60, 70])

#remove the last element
my_list.pop()

#sort in ascending order
my_list.sort()

#find and print the index of the number 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)


