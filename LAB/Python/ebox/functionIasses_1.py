def multiply(argument1, argument2=10):
    return argument1 * argument2

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

result1 = multiply(a)
print(f"The result is {result1}")

result2 = multiply(a, b)
print(f"The result is {result2}")

result3 = multiply(a, 9)
print(f"The result is {result3}")
