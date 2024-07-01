class Car:                                
    #Class is a blueprint
    #In this blueprint, there are properties and methods
    #properties tell what are the attributes
    #methods tell what are they can do or function
    
    #Propertise or Attributes:
    def __init__(self, brand, typ, year):
        
        self.brand = brand
        self.typ = typ
        self.year = year
    

    #Funtions or What the can do:
    def drive (self):
        print("The "+typ+" can be drive")
    
    def stop (self):
        print("The "+typ+" can be stopped")
