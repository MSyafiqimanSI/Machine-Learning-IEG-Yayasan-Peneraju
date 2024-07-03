def keyboardInput(datatype, caption,errormessage):
    value = None
    isInvalid = True
    while (isInvalid):
        try:
            value = datatype(input(caption))
        except:
            print(errormessage)
        else:
            isInvalid = False
    return value


def calculateSimpleInterest():
    principle = keyboardInput(int, "Principle Amount: ", "Principle must be an Integer")
    rate = keyboardInput(float,"Rate in Percentage: ", "Rate must be Float")
    period = keyboardInput(float, "Period in years: ", "Period must be Float")
    interest = (principle * rate * period) / 100
    print("Simple Interest: ", interest)
    print("Total Amount to be Paid: ", principle + interest)


print("="*90)
calculateSimpleInterest()
print("="*90)