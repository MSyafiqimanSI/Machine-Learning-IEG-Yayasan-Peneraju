def add (a, b):
    #result is a local variable
    #a variable created inside a function
    #this variable cannot be access from outside the function
    result = a + b

#this is called as scope of variable
#the main context is also called global context
x = 10
#variable x is created at the main context or global context
def printX ():
    #can i access the variable x creatd at the main context
    # inside the function context print(x)
    print("insides function",x)

printX()
print(x)

def modifyX():
    #now we are trying to modify the value of the variable x
    #the moment you try to modify a variable inside function
    #the variable is immediately created at the local context (inside function modifyX)
    #it does not refer to the global context
    x = 15
    print("inside modify:", x)


modifyX()
print(x)

#if you really want a function to modify the variable
#in the global context then the function must return the value 
#which again muat be assigned to the global 

def traditionalmodifyX():
    x = 15
    return x

x = traditionalmodifyX()
print(x)
#this the proper programming recommendation
#howevr in python we also have a short cut
#because if you follow the traditional method, function always return single value
#which means we can modify only 1 at a time
#how about I want to modify more tha  1 value??

def pythonmodifyX():
    global x #youre telling dont create x locally
    x = 25
    print("inside pythonmodify:", x)

pythonmodifyX()
print(x)

#let us discuss about scope of variable in the function context

def simpleInterest (principle,period,rate):
    result = 0
    def printSimpleInterest():#inner function
        #dont create local variable when modifying the value of the
        #outer value of the variable in other word
        #u can modify the variable which is in the outher function.
        nonlocal result
        temp = 0
        print("Simple Interest:", result)#however inner function can access the 
        #variable from outer func.
        print("Period:", period)
        print("Rate:", rate)
        #can i modify the variable result
        result = result + 50
        #print(temp) #now allowed
    result = ((principle * period) /100)

    printSimpleInterest();

simpleInterest(1000,1,6)

#Summary:
#Global keyword allows the function to modify the variable which is
#in the global context
#local keyword allows the inner function to modify the variable which is
#in the outer function context

fruit = "apple"
def myfunction():
    print(fruit)#in this case this varianle is suppose to be created locally
    #in this case we are referring to a varible which is not initiallized
    #fruit = "orange"


myfunction()