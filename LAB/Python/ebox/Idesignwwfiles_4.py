def inpt_file(filename):
    with open (filename,"r") as file:
        input_string = file.read()
        return input_string
        

def outpt_file(filename2, input_string):
    with open(filename2, "w") as file:
         reversed_string = input_string[::-1]
         file.write(reversed_string)
         return reversed_string
    


filename = "input.txt"
filename2 = "output.txt"


# filehandler = open(filename, "xt")
inpt_file(filename)
input_string = inpt_file(filename)
reversed_string = outpt_file(filename2, input_string)

print(f"Input string: {input_string}")
print(f"Reversed string: {reversed_string}")

        