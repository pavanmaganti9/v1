class Person:
    countnofinstance = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.countnofinstance += 1

    def person_details(self):
        print("Name is : ",self.name)
        print("Age is : ", self.age)

p1 = Person("Pavan",31)
p2 = Person("Bindu",26)

p1.person_details()
p2.person_details()

print("Instances:", Person.countnofinstance)
