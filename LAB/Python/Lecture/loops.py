#Whenever you wanna iterate a list of items, use 'for loop'
fruits = ["Apple", "ramburan",  "Orange", "durian", "mango", "cempedak","banana", "mangosteen", "grapes"]

for fruit in fruits:
    print(fruit)
#print all of the items in the even position
# for fruit in fruits[::2]:
#     print(fruit)
# print("=*"*50)
# #print 5 times
# for fruit in fruits:
#     if (len(fruit) == 6):
#         print(fruit)

#Iwant to crate a multiplication table of 5
#I want to until 12
# multipliers = [1,2,3,4,5,6,7,8,9,10,11,12]
# multiplicant = 5
# for multiplier in multipliers:
#     print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)

#print(list(range(1,13)))#range func takes start index and end index and generate numbers btween them



multiplicant = 10
multipliers = range(1,13)
for multiplier in multipliers:
    if multiplier % 5 == 0:continue
    #what continue keyword will do is
    #without executing
    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)
   

#split the digit in the input and print them
#let's
# givenNumber = 97409
# while (givenNumber > 0):
#     print(givenNumber % 10)
#     givenNumber //= 10
    
# print("="*50)
# givenNumber = 67891
# strGivenNum=str(givenNumber)
# for digit in strGivenNum:
#     print(digit)

