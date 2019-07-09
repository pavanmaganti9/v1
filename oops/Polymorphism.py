class dog:
    def sound(self):
        print("Bow Bow")

class cat:
    def sound(self):
        print("Meow")

def animalsound(ani_type):
    ani_type.sound()

catobj = cat()
dogobj = dog()

animalsound(catobj)
animalsound(dogobj)