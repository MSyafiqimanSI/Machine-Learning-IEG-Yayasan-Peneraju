x = 11

# if x % 2 == 0:
#     print("Given Number is {x}")

# print("even number")


# principle = int(input("Principle: "))
# period = int(input("period: "))
# rate = int(input("rate: "))
# interest = (principle * period * rate)/100
# print("Interest:", interest)


#runtime error
#

try:
  principle = int(input("Principle: "))



except ValueError:
     print("Print amount must be an Integer")
     principle = int(input("Principle: "))


except Exception as e:
   print("Something went wrong", e)

else:
   #the code inside the else block get 
   #executed only when there is no error
   print("All is well")

finally:
   #will always get executed regardless
   #of whether an error occur or not
   print("Thank you")




# principle = int(input("Principle: "))
period = int(input("period: "))
rate = int(input("rate: "))
interest = (principle * period * rate)/100
print("Interest:", interest)