#HAS-A Relationship
#Customer has a passport#

class Passport:

    def __init__(self,country, passportnumber):
        self.country = country
        self.passportnumber = passportnumber

    def __str__(self):
        return f"Country: {self.country}\n Passport Number: {self.passportnumber}"



class customer:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = " "
        self.passport = None
    
    def __str__(self):
        message = f"First Name: {self.firstname}\n"
        message = message + f"Last Name:{self.lastname}\n"
        message = message + f"IC Number: {self.icnumber}\n"
        
        if (self.passport != None):
            message = message + self.passport.__str__()
            return message




peter = customer("Peter", "Parker") #Parent
passport = Passport("UK", "E202089029") #Child
peter.passport = passport # HAS-A Relationship

print(peter)
print(peter.__dict__)

