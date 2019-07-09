class Person:
    def __init__(self):
        self.name = 'Bindu'
        self.__lastname = 'Pavan'

    def PrintName(self):
        self.__surName()
        self.__surName()
        return self.name + ' ' + self.__lastname

    def __surName(self):
        print("Maganti")


# Outside class
P = Person()
print(P.name)
print(P.PrintName())
#print(P.__lastname)
#print(P.__surName)