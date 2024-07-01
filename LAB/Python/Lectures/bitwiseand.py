# how to represent binary numb in python
# you can use ob followed by the binary number
# however it is still an integer
# by adding 0b, it will indicate the following value as a binary number.
# so in this case 0b111 is a binary 111 not as one-hundred and eleven.
ownerpermission = 0b111
print(ownerpermission)

filepermission = 0b111101001 #now owner can rwx, group can r and e, others can execute only (rwx = Read, Write, Execute)


#in data science/machine learning, when u were given categorical data you must convert them to data
#Which machine can understand
#this itself called "feature engineering"; gender;01 for male, 10 for female or race;1000 for malay, 0100 for chinese

#this bit extraction can be use using bitwise and operator
mask = 0b000111000
print(bin((filepermission & mask)>>3))

#in order to perform bit extraction we use 'bitwise and  &' operator
#111101001 - filepermission       original data
#000111000 - mask                 our mask
#000101000 - result/print         4,5,6 bits extracted from filepermission by using mask
#shift it to the right 3 timnes   000000109

#what if bitwise or '|' :
#111101001 - filepermission       original data
#000111000 - mask                 our mask
#111111001 - result/print         4,5,6 bits extracted from filepermission by using mask
#shift it to the right 3 timnes   000000109

#in conclusion, bitwise and is for extracting while bitwise or is for modifying data.
#please remember that there is no way to set a specific bit to 0 using bitwise or operator
#bitwise OR is also used inn extracting region of interest in an image

#what if biwise xor '^' :
#111101001 - filepermission       original data
#000111000 - mask                 our mask
#111010001 - result/print         4,5,6 bits extracted from filepermission by using mask
#shift it to the right 3 timnes   000000109
#bitwise Xor is used for enscryption
message = 0b01001010
key = 0b0101100
encrypted_msg = message ^ key
print(bin(encrypted_msg))

decrypted_msg = encrypted_msg ^ key
print(bin(decrypted_msg))

# 1s compliment
givenNumber = 5
# 5    0101
#1s complement is nothing but flip 0 to 1, 1 to 0
# 0101 = 1010
#2s complement  = 1s complement + 1
print(~givenNumber + 1) #1s compliment
print(-givenNumber) #unary negative
print(+-gu)