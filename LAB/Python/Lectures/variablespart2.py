#so far we have learnt how to assign single value to a single variable.
#We also learn how to assign multiple values to multiple in the same line.
#x = 10
#x, y = 10, 11

#How we are going to learn how to assign multi lines
# to a single var
#lets say we want to go for shopping
# senang citer array (malas nak taip panjang2)
fruits = ["Apple", "Orange", "mango", "banana", "grapes"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])

#how many items are on the list?
#use the built n function 'len'
print("Number of items we have:", len(fruits))

#how to find the max index?
print("Maximum index:", len(fruits) -1)

#index also can be a negative number
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])
print(fruits[-5])

#Range start_index:end_index
print(fruits[1:3])
print(fruits[1:4])

#what if we did not mention the start index
print(fruits[:4]) #it will start from  0

#what if we did not mention the end index
print(fruits[1:]) #it will start from  0

#in the range we can hv thurd number which represent is the step up value

fruits = ["Apple", "ramburan",  "Orange", "durian", "mango", "cempedak","banana", "mangosteen", "grapes"]
print(fruits[0:9])

#step-up:
print(fruits[0:9:2])
print(fruits[0:9:3])
print(fruits[0:9:4])#these features are important for us to take samples

#we also can use negative
print(fruits[-5:-1])
print(fruits[-1:-5])
print(fruits[-5:-1:-1])
print(fruits[::-1])