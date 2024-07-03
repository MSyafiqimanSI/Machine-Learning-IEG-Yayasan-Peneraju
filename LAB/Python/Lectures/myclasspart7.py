#Multiple inheritance

class Card:
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside Card Class")


class ATMCard(Card):
    def __init__(self):
        pass
    # def doSomething(self):
        #pass
        # print("Inside ATM Card Class")
        

class CreditCard(Card):
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside Credit Card Class")


class DebitCard(Card):
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside Debit Card Class")


class BankCard(ATMCard, CreditCard, DebitCard):
    def __init__(self):
        pass
    def doSomething(self):
        # print("Inside Bank Card Class")
        super().doSomething()

                                          
#We have created 5 classes
# and in all 5 classes we have dosomething method
# and it is implemented (got code inside which is "print()"
# 
# Let us create instance of the l;ast card:
bankCard = BankCard()
bankCard.doSomething()
#noiw remove the print statement from bankCard.doSomething
# and add/call super().doSomething()
#This time you will see "Inside ATM Card Class(Which is inherited 
#What if  i dont want to inherit from the base class called object
# you will loose all the default feature of a class
# #
