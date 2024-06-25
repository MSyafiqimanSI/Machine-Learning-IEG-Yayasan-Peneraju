#there are four different types of built-in data structure in python
#they are list, tuple, and dictionary

#list uses []
#list is modifiable (append,edit, delete)
#list is ordered (the items retain its position)
#list is indexed (0,1,2,3,...)
#list allows duplicate
#
fruits = ["apple", "orange", "mango", "banana", "grapes"]
#fruits is assigned with multiple values
#fruits is also called object
# if anything is object means it is in instance of a class
print(fruits)

#Modifiable
fruits.append("durian")
#the item gets added as last item
print(fruits)

#insert items inside the existing list
fruits.insert(1,"rambutan")
print(fruits)

fruits.insert(3, "cempedak")
print(fruits)

fruits.insert(5, "dummy")
print(fruits)

#update items in the list
fruits[5] = "mangosteen";
print(fruits)

#how to remove an item from the list
fruits.remove("durian")
print(fruits)

#how to remove the last item you can use the method pop
fruits.pop()
print(fruits)

#delete an item by index
#we can delete anything from memory permanently using the keyword 'del'
greeting = "Good Morning"
del greeting
#there is no () after del so it is confirm a KEYWORD

# print(greeting) #NameError
# print([1,2,3,4,5] + 5) #TypeError

del fruits[3]
print(fruits)

#If you want to clear the list(remove items inside of the list)
fruits.clear()
print(fruits)

#removing/deleting the entire list
del fruits
# print(fruits)

fruits = ["apple","mango", "orange", "mango","mango", "banana", "grapes", "apple"]
print(fruits.index("mango"))

newfruits = fruits[2:]
print(fruits.index("mango")+1)

#Enumerate is an iterable object
#but print dont know how to iterate the enumerate obj
#however we can typecast the enumerate objcts to a list using list function
print(list(enumerate(fruits)))
#
#
for item in enumerate(fruits):
    if item[1] == "mango":
        print("Mango is in position:", item[0])

print("total number of apples:", fruits.count("apple"))

#function that helps to sort the list alphabetical flow
fruits.sort()
print(fruits)

#reverse the list
fruits.reverse()
print(fruits)

#Deep Copy
x = [10,20,30,40,50]

y = []
for i in x:
    y.append(i)
print("="*90)
print(x)
print(y)
x[2]= 70
print(x)
print("="*90)
#infact you no need to use for loopx = [10,20,30,40,50]
y = x.copy
x[1] = 120
print(x)
print(y)
print("="*90)
#fruits is an instance of a list class
#Technically the objects are cretaed by calling the class
x = list([1,2,3,4,5])
print(x)
#however to create a list instead of using class, they let you use []
x = [1,2,3,4,5]
print(x)

#to invoke or call the operator whe use is '()'
#to call builtin function we use 'functionname ()'
#however int(), float(), type(), list(), etc are not function
#to call a function inside a module, we use sys.path()
#to call method inside in an object we use "string".split(), variable.sort, 
# list.append(), list.index(), list.reverse()


#to create a tupple we also use ()



