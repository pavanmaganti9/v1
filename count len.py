def string_length(my_string):
    """returns the length of a string
    """
    counter = 0
    for char in my_string:
        counter += 1
    return counter

# taking user input
#string_input = input("enter string : ")
string_input = ['Pavan','Bindu']
length = string_length(string_input)

print("length is ", length)
print(help(string_length))

a_string="abcd 123"
counter = 0
for letter in a_string:
    print(letter)
    counter += 1
    print(counter)