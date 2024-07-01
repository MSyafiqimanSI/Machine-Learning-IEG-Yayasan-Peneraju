#python has a buil.t in function call input
#the input func takes a single parameter (caption / question)
#input function will display the caption
#and wait for the user input
#The user will provide the input and press enter key
#the input is always provide the input and press enter kley
# firstNumber = input("Please key in the first number: ")
# print (firstNumber + " years old")
# #it's always return in string datatype
# print(type(firstNumber))

# secondNumber = input("Please key in the second Number: ")
# print(firstNumber + secondNumber) #string concatentenation
# print(int(firstNumber) + int(secondNumber)) #addition
numbers = input("enter: ")
numberlist = numbers.split(",")
print(numberlist)

total = 0
for number in numberlist:
    total = total + int(number)
print(total)