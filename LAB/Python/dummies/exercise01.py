#Given number is 97531
#I want to reverse the number; 13579

a0 = 97531
result = a0 % 10 # To find the remainder which is 1
a1 = a0 // 10 # To find the quotient which is 9753
print(result,a1)

result = (result * 10) + (a1 % 10) # (10) + (REMAINDER FROM 9753 DIVIDED BY 10 = 3)
a2 = a1 // 10
print(result,a2)

result = (result * 10) + (a2 % 10)
a3 = a2 // 10
print(result,a3)

result = (result * 10) + (a3 % 10)
a4 = a3 // 10
print(result,a4)

result = (result * 10) + (a4 % 10)
a5 = a4 // 10
print(result,a5)

#Akmal's solution
a0 = 97531

result = (a0 % 10) * 10000
result = result + ((a0//10) % 10)* 1000
result = result + ((a0//100) % 10)* 100
result = result + ((a0//1000) % 10)* 10
result = result + ((a0//10000) % 10)* 1
print (result)

#Another way
givenNumber  = 97531
result = 0
result = givenNumber % 10 # 1
givenNumber //= 10
result = result * 10 + givenNumber % 10

givenNumber //= 10
result = result * 10 + (givenNumber)

givenNumber //= 10
result = result * 10 + (givenNumber)

givenNumber //= 10
result = result * 10 + (givenNumber)

givenNumber //= 10
result = result * 10 + (givenNumber)

