#You should not hardcode the data inside the program
#fruits = ["apple, "orange#, "mango"]
#ypu must keep apple, orange, mango in a text file or csv file or excel file
#you must write a python program to read the data
#from the file and do the necessary things(print/process)
#in other words data must be separated from the program

 
# you must create a file using python code
#you can use the keyword open#
# open('fruits.txt')
#the open builtin function takes 2 parameters
#1) filename and 2)mode
#we hv to give instruction to python if the
#the file does not exist
#create it
#we call such extra instruction as mode
#Mode
#1. x create the file if it does not exist
#2. t this file is going to be text file
#3. b this going to be binary file
#4. w this will let us to write, however it will clear the existing content inside the file.
##
# open ('fruits.txt', 'xt')
#when you run it again it will error
#because the file already exists
#we suppose to checj wheteher the file
#already exists

# import os
# os.path.exists('filename')
# from os import path
# path.exists('filename')

from os.path import exists

def keyboardInput(datatype, caption, errorMessage, defaultValue=None):
    value = None
    isInvalid = True
    while (isInvalid):
        try:
            if defaultValue == None:
                value = datatype(input(caption))
            else:
                value = input(caption)
                if (value.strip()==""):
                    value = defaultValue
                else:
                    value = datatype(input(caption))
        except:
            print(errorMessage)
        else:
            isInvalid = False
    return value

def doMenu(filename):
    choice = -1
    while choice != 0:
        print("-----------")
        print("|0  -  Exit |")
        print("|1  -  List |")
        print("|2  -  Add  |")
        print("|3  -  Edit |")
        print("|4  - Delete|")
        print("------------")
        choice = keyboardInput(int, "Choice(0,1,2,3): ", "Choice must be Integer")
        if (choice == 0):
            print("Bye2")
        elif (choice == 1):
            printProduct(filename)
        elif (choice == 2):
            addProduct(filename)
        elif (choice == 3):
            editProduct(filename)
        elif (choice == 4):
            deleteProduct(filename)



filename = "fruits.txt"

# if not exists(filename):
#     open(filename, "xt")

def createFile(filename):
    if not exists(filename):
        try:
            filehandler = open(filename, "xt")
        except Exception as e:
            print("Something went wrong when we create the file:", e)
        else:
             createTitle(filename)
        finally:
            filehandler.close()


def createTitle(filename):
    try:
        with open(filename, 'wt') as filehandler:
            filehandler.write("Product|Quantity|Price")
    except Exception as e:
            print("Something went wrong when we create the title:", e)
    finally:
            filehandler.close()

def addProduct(filename):
    try:
        product = keyboardInput(str, "Product: ", "Product must be string")
        quantity = keyboardInput(int, "Quantity: ", "Quantity must be interger")
        price = keyboardInput(float, "Price: ", "Price must be float")

        with open(filename, "at") as filehandler:
            filehandler.write(f"\n{product}|{quantity}|{price}")
    except Exception as e:
        print("Something went wrong when we append the product:", e)

def printProduct(filename):
    try:
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            product, quantity, price = line.strip().split("|")
            if (index == 0):
                print(f"{"No:":<5}{product:20}{quantity:>20}{price:>20}")
                print("=" * 80)
            else:
                print(f"{index:<5}{product:20}{int(quantity):>20}{float(price):>20.2f}")
    except Exception as e:
        print("Something went wrong when we print the products", e)

def editProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filerhandler:
            lines = filerhandler.readlines()
        data = []
        for line in lines:
           data.append(line.strip().split("|"))
        index = keyboardInput(int, "Index of Product:", "Index must be INT")
        if (index >= len(data)):
            print("Sorry not available :(")
        else:
            product, quantity, price = data[index]
            print(f"Product: {product}\nQuantity: {quantity}\nPrice: {price}")
            confirm = keyboardInput(str, "Are you sure? (y/n): ", "Incorrect response")
            if (confirm == "y"):
                newproduct = keyboardInput(str, f"Product[{product}]: ", "Product must be string")
                newquantity = keyboardInput(int, f"Quantity[{quantity}]: ", "Quantity must be interger")
                newprice = keyboardInput(float, f"Price[{price}]: ", "Price must be float")
                data[index] = [newproduct, newquantity, newprice]
                newlines = []
                for product in data:
                    line = "|".join(map(str, product)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)
    except Exception as e:
        print("Something went wrong when we edit the products", e)


def deleteProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filerhandler:
            lines = filerhandler.readlines()
        data = []
        for line in lines:
           data.append(line.strip().split("|"))
        index = keyboardInput(int, "Index of Product:", "Index must be INT")
        if (index >= len(data)):
            print("Sorry not available :(")
        else:
            product, quantity, price = data[index]
            print(f"Product: {product}\nQuantity: {quantity}\nPrice: {price}")
            confirm = keyboardInput(str, "Are you sure you want to delete? (y/n): ", "Incorrect response")
            if (confirm == "y"):
                del data[index]
                newlines = []
                for product in data:
                    line = "|".join(map(str, product)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)
    except Exception as e:
        print("Something went wrong when we edit the products", e)


filename = "fruits.txt"
createFile(filename)
doMenu(filename)

# addProduct(filename)
# printProduct(filename)


