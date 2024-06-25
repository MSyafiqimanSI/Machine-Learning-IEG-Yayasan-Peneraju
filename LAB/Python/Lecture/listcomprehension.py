# #deep copy
# fruits = ["apple", "orange", "mango", "banana", "grapes"]
# #overseafruits = fruits #you shouldnt do this

# for fruit in fruits:
#     print(fruit)


# multiplesofthree = []
# for number in range(1,50):
#     if number % 3 == 0:
#         multiplesofthree.append(number)


# numbers = [2,5,7,3,46,10,11,15,17,24,22]
# oddnumbers = []
# evennumbers = []
# for number in numbers:
#     if numbers % 2 != 0:
#         oddnumbers.append(number)
#     else:
#         evennumbers.append(number)



# sum = 0
# for number in range(1,10):
#     sum = sum + number

# mean = 0
# for number in range(1,10):
#     mean = mean + number
# mean = mean / len(range(1,10))



# priceswithsst = [price + (price*0.06) for price in prices]


# #using list comprehension
# oddnumbers = [number for number in numbers if (number % 2 != 0)]
# print("Odd Numbers:", oddnumbers)

# priceswithsst = [price + (price*0.06) for price in prices]
# print(pricewithsst)

# multiplesofthree = [for number in range(1,50) if (number % 3 == 0)]
# print(multiplesofthree)

# #task which we need to do is find price wth sst
# #now using the above 
# def CalculateSST(price):
#     priceswithsst = price + (price * 0.06)
#     return priceswithsst

# #this map function takes 2 parameters
# #1st parameter is the function and second parameter is the list

# priceswithsst = map(CalculateSST, prices)
# #what map does
# # inside map there is af for loop which pulls out the price from prices
# #and pass the price to our function. Our function return the price with sst.
# #finally once all the prices are iterated the map function returns the list
# #def map(func, values):

# def map(func, values)
# result = []
# for value in values:
#     result.append(func(value))
# return result

# # def fahrenheitToCelcius (fahrenheitvalue):
# #     return(fahrenheitvalue - 32)*59





# def findMultipleofThree (number):
#     return True if (number % 3 == 0) else False

# multiplesofthree = filter(findMultipleofThree, range(1,50))
# print(list(multiplesofthree))



# def isOddNumber(number):
#     return True if (number % 3 == 0) else False

# oddnumbers = 







#reduce is not a builtin function
#it is inside of the module called itertools
from functools import reduce


numbers = [1,2,3]


def findTotal (oldvalue, currentvalue):
    return oldvalue + currentvalue

print(reduce (findTotal, numbers))

#reduce functions takes another functions as first parameter
#that function suppose to take 2 parameter
#reduce function takes list as second parameter
# def reduce (func, numbers):
#     sum = 0
#     for number in numbers:
#         sum = func (sum, number)
#     return sum

def factorial(oldvalue, currentvalue):
    return oldvalue * currentvalue

print(reduce(factorial, numbers))

print(reduce(factorial, numbers, 5))