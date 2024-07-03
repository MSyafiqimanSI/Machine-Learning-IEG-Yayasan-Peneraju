#Encapsulation
#Encapsulate the properties inside the class
#in other languages we have keywords public, private, protected 
###

class circle:
    def __init__(self, radius):
        # change the property wth single underscore
        # this makes the property private
        self.__radius = 0
        if(isinstance(radius,int)):
            self.__radius = radius
        
        else:
            print("invalid Radius")
        self.__radius = radius
        self.__radius = radius
        print("Number")
    
    #getter and seter method
    def getRadius(self):
        return self.__radius
    
    def setRadius (self, radius):
        if (isinstance(radius ,int)):
            self.__radius = radius
        else:
            print("Invalid Radius")

    
    

    def area(self):
        return 3.14 * self.__radius * self.__radius
    
    def circumference(self):
        return 2 * 3.14 * self.__radius 
    
    def __str__(self):
        return f"Radius of this circle is {self.__radius}"
    
    #property is a class
    #invoking the class by passing the method                                          
    radius = property(getRadius, setRadius)
  
mycircle  = circle(20)
print(mycircle.getRadius)
mycircle.setRadius(50)
print(mycircle)
mycircle.__radius  = 30
# print(mycircle)
# print(mycircle.area())
