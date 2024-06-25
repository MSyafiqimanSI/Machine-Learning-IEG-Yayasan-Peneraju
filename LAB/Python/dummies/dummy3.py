# range(2,51)
# count = 0
# print(1)
# givenNumber = 2

# while count < 10:
#     isPrime = True
#     divisors = range(2,givenNumber)
def orderdinner(makan,minum):
    prices = []
    for food in makan:
        if food == "nasi ayam":
            prices.append(5.5)
        elif food == "nasi lemak":
            prices.append(5.0)
        elif food == "mee hailam":
            prices.append(7.0)
    for drink in minum:
        if drink == "teh ais":
            prices.append(2.5)
        elif drink == "kopi ais":
            prices.append(2.5)
        elif drink == "teh o ais":
            prices.append(2.0)
    return prices
#####################################################

ordermakan = orderdinner(["nasi ayam"], ["teh ais"])
totalPrice = 0
for price in ordermakan:
    totalPrice = totalPrice + price
print("Total price is: ", totalPrice)




        