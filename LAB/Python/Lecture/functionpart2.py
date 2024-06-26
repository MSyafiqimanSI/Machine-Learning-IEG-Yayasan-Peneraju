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