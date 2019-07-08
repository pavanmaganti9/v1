class Dad:
    def father(self):
        print("Dad is my hero!")

class Mom:
    def mother(self):
        print("Mom is everything!")

class Me(Dad,Mom):
    def myself(self):
        print("This is me with mom and dad!")

pavan = Me()
pavan.mother()
pavan.father()
pavan.myself()