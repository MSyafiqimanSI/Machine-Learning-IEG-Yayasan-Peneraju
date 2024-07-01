# principle = 1000
# period  = 1
""""
def calculateSimpleInterest (principle, period, rate):
    simpleInterest = (principle * period * rate)/100
    return simpleInterest
"""
class Student:
    #In python we cannot declare properties (variable)
    #without assigning a  value
    #There is a special methof(function) called constructor
    
    #This method gets called everytime when you cretae an object of this class (instance of this class)

    #Since it is a special method it must have double underscore
    #followed by 'init' and 'gain' followed by double underscore
    #Difference between method and a function:
    # 1) 

    def __init__(self):
        print("Object is created")
    
    def attendClass(self):
        print("Object started attending the class")

    def doProject(self, projectname):
        print("Object started doing the project:", projectname)
    
    def attendExam(self, exam):
        grade = "A"
        return f"Object has attended the exam: {exam} and obtaine the score {grade}"
    


#Let us create our first object
zul = Student()

zul.attendClass()

zul.doProject("Pokemon")
print("="*50)

zul.attendExam("Python 102")
print(zul.attendExam("Python 102"))

