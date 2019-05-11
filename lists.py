x1 = [1,2,3]
print(type(x1))

print(x1[1])

"""
Functions of Lists
"""

#append function : When we add an item to list using append. By default the item will be added to the end of the list

new1 = [1,2,3,4,5]
new1.append(31)

print(new1)

#insert function : When we add an item to list using insert function.
# insert(i, x) is the syntax we can insert as per the index we want and inserts in the position.

new2 = [1,2,3,4,5]
new2.insert(0,31)
print(new2)

new2.insert(3,99)
print(new2)