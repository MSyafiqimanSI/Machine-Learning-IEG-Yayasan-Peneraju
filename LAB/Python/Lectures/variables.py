#product is the variable
#"Television" is the string value/literal
#To differentiate the variables from the string, we use single or double quote
product = "Television"
quantity = 2
price = 1455.25 
available = True #True and False (boolean value/literal)

print("Product:", product)
print("Quantity:", quantity)
print("Price:", price)
print("Available:", available)

#type is a built-in function that tell us what is the data type 
#of the variables (dynamically assigned by python)
print(type(product))
print(type(quantity))
print(type(price))
print(type(available))

total = quantity * price 
print("Total:", total)

quantity = "10"
print(type(quantity))
#print(quantity*price)

#to convert str to int we hv a built-in func,
total = int(quantity)*float(price)
print(total)

#in python u can have 
x, y = 101, 102

#you can also have this
x, y = 101 + 1, 102 + 1

#In some programming langguage you can initialize or you can 
# #assign multiple variable with a single value
x, y = 105 #however this is not allowed
#You cannot 
y = 0
y = ""
y = None #Non-type