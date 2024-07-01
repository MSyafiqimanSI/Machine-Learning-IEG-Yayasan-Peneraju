#Functions are used to organize our code
#functions are not for solving problems like 'if', 'for', 'while', etc

#When to create our function?
#whenever you copy and paste a block of code
#then you know already it has to be a function
print("Hello World !!!")

def sayHelloWorld():
    print("HelloWorld inside the func!!!")

sayHelloWorld()


####
def greeting(name):
    print("Good Morning", name)

name = input()
greeting(name)
greeting("Jegan")
greeting("Anwar Ibrahim")
greeting("Najib Razak")
greeting("Micheal Jackson")
print("="*60)

def total(x, y, z):
    result = x + y + z
    print("Result", result)

total(10, 20, 30)
print("="*80)

def arithmatic(a,b):
    w = (4*a) + 7
    valuen = w*10 + b
    print(valuen)

arithmatic(5, 3)
print("="*80)

def buyLunch(makan,minum):
    prices = []
    for food in makan:
        if (food == "nasi"):
            prices.append(2.80)
        elif (food == "sayur"):
            prices.append(2.50)
    for drink in minum:
        if (drink == "nescafe"):
            prices.append(2.50)
    return prices
##################################
#total price:
itemprices = buyLunch(["nasi", "sayur"], ["nescafe"])
total = 0

for price in itemprices:
    total = total + price
print("Amount to be paid:", total)
print("="*60)

def participantList(nameone, nametwo, namethree):
    nameone = nameone + "Data Science"
    nametwo = nametwo + "Data Science"
    namethree = namethree + "Machine Learning"
    return nameone,nametwo,namethree

result = participantList("John", "Peter", "Parker")
print(type(result))
print(result)
#tuple is  nothing but only read only list
print("="*60)

def calculateSimpleInterest(principle,period=1,rate=6):
    interest = (principle * period * rate)/100
    return interest

print(calculateSimpleInterest(1000))
print(calculateSimpleInterest(1000,2))
print(calculateSimpleInterest(principle=1000, rate=5))
print("="*80)
###########################################################

def findTotal(givenNumbers):
    total = 0
    for givenNumber in givenNumbers:
        total = total +givenNumber
    return total


#Variable length Argument
#the number of arguments which we pass varry
#caller can pass the value as a list
print(findTotal([10,20,30,]))
print(findTotal([10,20,30,40,50,60]))
print(findTotal([10,20,30,40,50,60,70,80,90]))
print("="*90)

#you can declare the parameter to be able accept any number by intoducing '*' infront of the parameter
#python will take all the arguments place them inside a list
#and pass the list to the function
"""""
def calculateTotal(givenNumbers):
    total = 0
    for givenNumber in givenNumbers:
        total = total +givenNumber
    return total

print(calculateTotal(10,20,30,))
print(calculateTotal(10,20,30,40,50,60))
print(calculateTotal(10,20,30,40,50,60,70,80,90))
############################################
"""
def listSixLetterFruits(*fruits):
    for fruit in fruits:
        if len(fruit) == 6: 
            print(fruit)

print(listSixLetterFruits("apple","orange", "mango","banana", "durian", "grapes"))