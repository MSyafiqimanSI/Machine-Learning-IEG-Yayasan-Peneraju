#Is-A Relationship 
# ##
class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = " "
class Alumni(Student):

    def __init__(self, firstname, lastname, alumninumber):
        Student.__init__(self, firstname, lastname) #IS-A Relationship
        self.alumninumber = alumninumber
        pass

    def __str__(self):
        return f"First Name:  {self.firstname}\
            \n Last Name: {self.lastname}\
            \n IC Number: {self.icnumber}\
            \n Alumni Number: {self.alumninumber}"

alumni = Alumni("Parker", "Peter", 980520)
print(alumni)
        
