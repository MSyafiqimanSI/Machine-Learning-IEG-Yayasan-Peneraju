#Polymorphism
#Polymorphism is the ability of a function to take on different forms.
#Polymorphism is a Greek word which means "having many forms".

class Gender:
    def __init__(self):
        pass
    def doCarryObjects(self):
        pass

class Male:
    def __init__(self):
        pass
    def doCarryObjects(self):
        print("Carry Heavy Objects")

class Female:
    def __init__(self):
        pass
    def doCarryObjects(self):
        print("Carry Light Objects")

def getGender (name):
    if "A/L" in name:
        return Male()
    else:
        return Female()
    

#Python dynamically set the data type for the gender variable
#sometimes it becomes Male object
#sometimes it becomes Female object#
gender = getGender("Khairi A/L Abu Bakar")
gender.doCarryObjects()
print("Khairi have to carry", gender.doCarryObjects())

gender = getGender("Aida A/P Abu Bakar")
gender.doCarryObjects()
