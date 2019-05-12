basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)
print(fruit)


a = set('abracadabra')
print(a)
b = set('alacazam')

res1 = a - b  # letters in a but not in b
print(res1)

res2 = a | b  # letters in either a or b
print(res2)

res3 = a & b   # letters in both a and b
print(res3)

res4 = a ^ b  # letters in a or b but not both
print(res4)


#set comprehension
a1 = {x for x in 'abracadabra' if x not in 'abc'}
print(a1)
