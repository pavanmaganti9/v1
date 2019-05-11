#normal procedure to calculate squares of the list
numbers = [1, 2, 3, 4]
squares = []

for n in numbers:
  squares.append(n**2)

print(squares)


#by using list comprehension

squares = [n**2 for n in numbers]

print(squares)