# firstName = "Khairi"
# lastName = "Abu Bakar"
# #Usually both sides of the operator is numbers
# #if they're number we can perform addition

# #IF BOTH SIDES ARE STRING WE CAN PERFORM "STRING CONCATENATION"
# fullName = firstName + "  " +lastName
# print(*fullName)

# carPlate = "JCG"
# number = 6979

# #however this use case e cannot add them because one is number and another one is string
# #So let us convert number to string by using 'str'
# carPlateNumber = carPlate + str (number)
# print(carPlateNumber)

# #In python we can multiply str with int
# #when we do this it will produce "times" effect
# product = "book"
# print(product * 5)
# print("=" * 100)

#So far we know how strings are enclosed by double and single quote
#We can also use triple double quote or triple single quote
#they are use to create multiline strings

#traditionally
# message = """As I am not feeling well I wont be able
# I won't able to attend the meeting
# Please proceed"""
# print(message)

# myfile1 = "c:\\newfolder\\table\\read.txt"
# print(myfile1)

# myfile2 = r"c:\newfolder\table\read.txt" #r is raw string
# print(myfile2)

#realtionship between string and lists
#strings are nothing but list of char
# mygreeting = "Hello world"
# print(mygreeting[0])
# print(mygreeting[0:6])
# print(mygreeting[::2])
# print(mygreeting[::-1])
# print(len(mygreeting))

#"Television " is a string literal and also called as string object
#Objects have functions inside
product = "Televisison cloths fruits vegetable"
product.split()
print(product.split())
#this func takes literal assigned to the var n split dem (tokenize them) into multi words (separated by space)
#since it is going to return more than  1 word its going to be list of words
#Functions inside the obj is also CALLED "Method"
#From now u say "print() is a function" and where "split is a a method"
