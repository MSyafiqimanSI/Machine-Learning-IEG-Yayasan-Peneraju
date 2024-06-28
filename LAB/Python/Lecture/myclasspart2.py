class Student:

    def __init__(self, firstname, lastname, icnumber):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = icnumber
        selfprogram = " "
        self.address = " "
    
    def attendClass(self):
        print("Object started attending the class")

    def doProject(self, projectname):
        print("Object started doing the project:", projectname)
    
    def attendExam(self, exam):
        grade = "A"
        return f"Object has attended the exam: {exam} and obtaine the score {grade}"
    
    def info(self):
        print("FirstName")

zul = Student("Ahmad","Zul", 9876543210,)
zul.attendClass()
zul.doProject("Pokemon")
zul.attendExam("Python 102")
print(zul.attendExam("Python 102"))
