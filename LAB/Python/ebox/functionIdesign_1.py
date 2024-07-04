def name_message(name,message = "Welcome to Python Programming"):
    print(f"Hello  {name}, {message}")

def num_options(x):
    if x == 1:
        print("Enter the name")
        name = input()
        print("Enter the message")
        message = input()
        name_message(name,message)
    elif x == 2:
        print("Enter the name")
        name = input()
        name_message(name)

print("Menu")
print("1. Name and Message")
print("2. Name")
x = int(input())
num_options(x)