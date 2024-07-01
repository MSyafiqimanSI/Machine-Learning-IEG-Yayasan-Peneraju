#function can have inner function
def sum(a,b):
    return a + b

x = 10


#Anonymous function assigned to a variable
# sum = def (a, b):
#     return a + b

def authenticate(username, password):     #this is outer function
    def calculatesSI(principle, period, rate):  #we can creat inner function
        result = (principle * period * rate) /100
        return result
    if (username == "admin" and password == "pwd123"):
        #since calculateSI function is inside authenticae function
        #we can still call this fnction here
        print("Simple Interes:", calculatesSI(1000,1,6))

#you can call the function which is inthis function context
authenticate ("admin", "pwd123")

#but you cannot call the function which is inside another function context
#calculateSI(100, 1, 6) #you cannot do this

#However if the outer function (authenticate)
#return the inner function (calculateSI)
#then we can call the inner function
func = authenticate("admin", "pwd123")
print("Simple Interest:", func(1000,1,6))

#we also can do like this:
print("Simple Interest:", authenticate("admin", "pwd123")(1000,1,6))

#Anonymous function

#however if you create a function without name how to call them? 
# So it is always good to assigned the anonymous function  to a variable
# sum = def (a,b):
    #return
#the above is n not valid syntax in python, however every functions are 
#handled by python itself
#That means in python evry function is an anonymous function

#they do have lambda which led you to create function in one line
#the functio  can onlu have 1 statement(line of code)
#def add(a, b): return a + b

#add def(a,b): return a+b