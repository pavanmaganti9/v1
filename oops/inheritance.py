class Inherit:
    def __init__(self,id):
        self.id = id

    def get_email(self):
        #print("Email from id : ", self.id)
        return "pavanmaganti87@gmail.com"

mail = Inherit("123456789")

#print(mail.get_email())
