givenNumbers = range(2, 51)
count = 9
print(1)


for givenNumber in givenNumbers:
    print(givenNumber)

    if count > 0:
        isPrime = True
        divisor = range(int(2,givenNumber))

    if divisor % givenNumber == 0:
        isPrime = False
        break

    if isPrime ==True:
        print(givenNumber)
        count = count - 1
    
    if count == 0:
        break