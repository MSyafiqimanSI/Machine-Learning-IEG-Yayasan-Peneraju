def nameandmessage(nama, message):
    print("Hello " + nama + " " + message)

def nameonly(name):
    print("Hello" + name + ",Welcome to python programming")


print("1. Name and Message")
print("2. Name")
a = input()

if a == 1:
    print("Enter the name")
    nama = input(" ")
    print("Enter the message")
    message = input(" ")
    nameandmessage(nama, message)

elif a == 2:
    name = input("")
    nameonly(name)
