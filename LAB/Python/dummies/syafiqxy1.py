# givenNumber = 98765

# result = givenNumber % 10 #5
# givenNumber //= 10 #9876
# result = (result*10) + (givenNumber % 10) #(5*10) + 6 = 56

# givenNumber //= 10 #987
# result = (result * 10) + (givenNumber % 10) #(56 * 10) + 7 = 567

# #givenNumber //= 10 #98
# #result = (result * 10) + (givenNumber % 10) #()
# #print(result)
num = "98765"
print(reversed(num))