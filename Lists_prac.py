listOfStrings = ['One', 'Two', 'Three', 'Four']
strOfStrings = ''.join(listOfStrings)
print(strOfStrings)

print(tuple(listOfStrings))

print(set(listOfStrings))

helloWorld = ['hello','world','1','2','Pavan']

print(list(zip(helloWorld)))

x = [1, 2, 3]
x.append([4, 5])
print (x)

x = [1, 2, 3]
x.extend([4, 5,'Pavan'])
print (x)

print(len(listOfStrings))

plusList = listOfStrings + [4,5]
print(plusList)