class Parent:
    def __init__(self,name):
        print('Parent init', name)

class Parent2:
    def __init__(self,name):
        print('Parent2 init', name)

class Child(Parent2, Parent):
    def __init__(self):
        print('child init')
        super().__init__('Pavan')
        Parent.__init__(self,'Bindu')
        Parent2.__init__(self, 'Latika')

child = Child()
print(Child.__mro__)