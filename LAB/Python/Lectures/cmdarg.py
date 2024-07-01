#when we call python to execute our program we can pass value our programs in the 
# command line which is also called command line arguments
# these arguments are separated by space
#All these argument inside the list are string type
#sys.argv give us alist, which contains command line passed to python
#in the list you can see the item at position 0 is program name itself
import sys 

cmdarguments = sys.argv # we are using '.'(dot operator) to access the variable which is iside the module sys
print(cmdarguments)

#find the total of the arguments
#if we know the total number of arguments we can hardcode it
# total = int(cmdarguments[1]) + int(cmdarguments[2])

#in this case we have to use loops (since we do not know the total  number of arguments)
total = 0
for number in cmdarguments[1:]:
    total = total + int(number)

print(total)
