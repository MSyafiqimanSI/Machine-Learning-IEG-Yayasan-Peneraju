# hexadecimalnumber = 0xF
# print(hexadecimalnumber)
# print(hex(hexadecimalnumber))

# print("=" * 50)

# octalnumber = 0o10
# print(octalnumber)
# print(oct(octalnumber))

# #question 1
# print("Question 1")
# x = 0b10101100
# maskx = 0b00001100
# print(bin(x & maskx))
# print("="*50)

# #question 2
# print("Question 2")
# y = 0b11011001
# print("Even Number") if (y % 2 == 0) else print("Odd Number")
# print("="*50)

# #question3
# print("Question 3")
# maskxa = 0b00001100
# print(bin(x & maskxa))
# print("="*50)

# #question4
# print("Question 4")
# print("It is a set") if (((y)>>4) & 1) else ("Not a set")

# #12 and 16
# a = 1/12
# b = 1/16
# wr = a + b
# wh = 1/wr
# print(wh, "Hours")

# #8 and 10
# c = 1/8
# d = 1/10
# wr1 = c + d
# wh1 = 1/wr1
# print(wh1, "Hours")
#=======================================================================
# Initialize two variables, a = 0b10101000 and b = 0b01010100.

# Write Python code to:

# Set the lower 4 bits of a.
# Combine the bits of a and b using OR.
# Create a mask to set the 2nd and 6th bits of a.

# a = 0b10101000 
# b = 0b01010100
# print("question 1")#qs1
# mask = 0b10100111
# print(bin(a & mask))
# print("="*50)

# print("question 2")#qs2
# print(bin(a | b))
# print("="*50)

# print("question 3")#3
# #10 1 010 0 0
# mask2 = 0b10001010
# print(bin(a ^ mask2))


# Initialize two variables, x = 0b10101100 and y = 0b11010010.

# Write Python code to:
# Swap the values of x and y without using a temporary variable.
# Toggle the 3rd and 5th bits of x.
# Check if two given numbers a = 29 and b = 15 are different.
# x = 0b10101100
# y = 0b11010010
# print("question 1")#qs1
# x = x + y 
# y = x - y
# x = x - y
# print("x=", bin(x))
# print("y=", bin(y))
# print("=" * 50)

x = 0b10101100
print(bin(x))
mask = 0b00010100
print(bin(x ^ mask))