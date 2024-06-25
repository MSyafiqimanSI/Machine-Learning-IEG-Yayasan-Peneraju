num = (int(input("Enter your number: ")))
original_num = num
if (num <= 100):
    b = num % 10
    a = num // 10
    print(a, b)
    asq = a**b
    bsq = b**b
    t = asq+bsq
    print (t)

elif (100 <= num <= 1000): #153
    c = num % 10 #3
    num //= 10 #15
    b = num % 10 #5
    a = num // 10 #1
    print(a, b, c)
    asq = a**c 
    bsq = b**c 
    csq = c**c 
    t = asq + bsq + csq
    print(t)

print("="*50)

if (t == original_num):
    print("Positively Armstrong Number")
else:
    print("Negatively Armstrong Number")