#Assignment Operators
x = 0
x += 1 #x = x+1 
x += 2 #x = x+2
x += 5 #x = x+5
x += x + 1 #x + (x+1)

print (x)

x -= 1 # x = x - 1
x *= 1
x /= 1
x //= 1
x %= 1

#Comparison Operators
myheight = 5.2
yourheight = 5.3
mysistersheight = 5.2

#Let us create a True statement:
print(yourheight > myheight)
print(myheight == mysistersheight)
print(mysistersheight < yourheight)
print(myheight != yourheight)

print(yourheight >= myheight)
print(myheight >= mysistersheight)

print(myheight <= yourheight)
print(mysistersheight <= myheight)

a = 21
b = 14
c = 7
print (a > b and a > c) # a is the greatest
print (c < a and c < b)

print (b > c and b < a or (b > a and b < c))

#Truth table

# '^' is an XOR Operator
print((a > c) ^ (a > b))

#Negation Operator (Not)
print(not(a > c)) # False
print(not(a < c)) # True


print("XOR:", (a > c) ^ (a > b))