num = int(input("Please enter your number: "))
x = num // 10
y = num % 10
swapped_num = y * 10 + x

print("Original number:", num)
print("Swapped number:", swapped_num)

ori_square = num**2
swap_square = swapped_num**2

print("Original number after square:", ori_square)
print("Swapped number after square:", swap_square)


number_str  = str(ori_square) #I try to convert the number to string, so its easy to reverse the squared ori_square

reversed_str  = number_str [2] + number_str [1] + number_str [0]

reversed_square = int(reversed_str )

if (swap_square == reversed_square): #This is where it determines the number is Adam number or not
    print(num, "is an Adam number")
else:
    print(num, "is not an Adam number")









    x = 5
    y = 1
    z = 6
    