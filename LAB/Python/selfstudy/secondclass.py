x = 100

#now i want to know the address location of the literal 100 is.
print(x)
#we can use a built in function called id
print(id(x))

y = 100
#however in python, the object 100 is not created first,python scan the memory if the 100 is already exist
#If yes, python will reuse the object rather than creating the new object
print(id(y))
print("aaaaaaaaaaaaaaaaaaaa")
#Same goes with any data type
a = "Hello"
b = "Hello"
print(id(a))
print(id(b))