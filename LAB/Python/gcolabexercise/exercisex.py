num = (int(input("Enter your number: ")))
num_sq = num**2

if (num < 100):
  x = num // 10
  y = num % 10
  rev = y * 10 + x
  print("Reversed: ")
  print(rev)

elif (100 <= num <= 999):
  rev = num % 10
  num //= 10
  rev = rev * 10 + num % 10
  num //= 10
  rev = rev * 10 + num % 10
  print("Reversed: ")
  print(rev)


elif (num > 1000):
  rev = num % 10
  num //= 10
  rev = rev * 10 + num % 10
  num //= 10
  rev = rev * 10 + num % 10
  num //= 10
  rev = rev * 10 + num % 10
  print("Reversed: ")
  print(rev)

rev_sq = rev**2
print(rev_sq)

if (rev_sq >= 10000):
  print("Value exceed Ten Thousand")

elif(100 <= rev <= 1000):
  rev2 = rev_sq % 10 #6
  rev_sq //=10 #291
  rev2 = (rev2 * 10) + (rev_sq % 10) #(6*10) * (291%10 == 1) == 61
  rev_sq //= 10 #29
  rev2 = (rev2 * 10) + (rev_sq % 10) #610 + 9 == 619
  print(rev2)

elif (rev_sq > 1000):
  rev2 = rev_sq % 10 #6
  rev_sq //=10 #291
  rev2 = (rev2 * 10) + (rev_sq % 10) #(6*10) * (291%10 == 1) == 61
  rev_sq //= 10 #29
  rev2 = (rev2 * 10) + (rev_sq % 10) #610 + 9 == 619
  rev_sq //= 10 #2
  rev2 = (rev2 * 10) + (rev_sq // 1) # 6190 + 2
  print (rev2) 
  
