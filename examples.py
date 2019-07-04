x = 'prep'
for i in range(len(x)):
    print(i)


def myfunc(a):
    a = a + 2
    a = a * 2
    return a
print(myfunc(2))

x = ['geeky', 'prep']
for k in x:
    k.upper()
print(x)

final={}
def push(x):
    if x in final:
        final[x] += 1
    else:
        final[x] = 1
push('Geeky')
push('Prep')
push('Geeky')
print (len(final))

G = ['a','b','c','d']
print("".join(G))


def addToList(listcontainer):
    listcontainer += [10]


sd = [10, 20, 30, 40]
addToList(sd)
print(len(sd))

dictionary = {}
dictionary[1] = 4
dictionary['1'] = 2
dictionary[1] += 1

calc = 0
for k in dictionary:
    calc += dictionary[k]

print(calc)


class Geeky:
    def __init__(self, id):
        self.id = id


manager = Geeky(100)

manager.__dict__['life'] = 497
manager.__dict__['wife'] = 200

x = manager.life +manager.wife + len(manager.__dict__)

print(x)

geeky1 = [1, 2, 3, 4]

geeky1.append([5, 6, 7, 8])

print(len(geeky1))


class gp:
    def __init__(x, y):
        x.y = y
        y = 555


s = gp(111)
print(s.y)

dictionary = {1:'1', 2:'2', 3:'3'}
del dictionary[1]
dictionary[1] = '10'
del dictionary[2]
print(len(dictionary))