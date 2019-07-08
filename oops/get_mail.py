from inheritance import *

class getmail(Inherit):
    def mail(self):
        print("Mail id is : ",self.id)
        print(mail.get_email())
        return mail.get_email(),self.id


m1 = getmail(5678)

print(m1.mail())

