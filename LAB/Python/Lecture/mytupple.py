#tupple is nothing but read only list
#tupple uses []
#it is not modifiable(cannot append, cannot edit, cannot delete)
#it is ordered
#it is indexed


x = (1,2,3,4,5)
print(x)
print(type(x))

#selection and  indexing
print(x[0])

#it is not modifiable
fruits = ("apple", "orange", "apple", "mango", "apple")
print("Amount of apples in fruits:", fruits.count("apple"))

#however you can delete the entire tuple using del keyword
#del x[0] # i repeat this not allowed

#tuple is does not hv many features as list
#why we use tuple: 1)take less space 2) faster than list
#normally python handles its list using tuple
def returnFruits():
    return "apple", "orange"

print(returnFruits)
print(type(returnFruits()))











#converting the list to tuple
#you pass the list tuple class it will return tuple object
x = [6,7,8,9]
x = tuple(x)
print(type(x))

#onelast feature in list
#list can auto explode
#explode means create 1 variable for every item in the list
fruits = ["apple", "orange", "mango"]
fruit01 = fruits[0]
fruit02 = fruits[1]
fruit03 = fruits[2]
#however in python you dont need to do it manually like this, instead;
fruit01, fruit02, fruit03 = fruits
#in other words we are assigning multi items in the list to multi variables

#there is a problem
a = (10)
#now python really confused ist it really tuple or expression
#python gives priority for expression than tuple
#automatically, 10 is an integer assigned to a
print(type(a))

#to ensre the data is in tuple format please add an extra comma
b = (10,)
print(type(b))




