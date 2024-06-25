print("Enter branding expenses")
bran = float(input(""))

print("Enter travel expenses")
trav = float(input(""))

print("Enter food expenses")
food = float(input(""))

print("Enter logistic expenses")
logi = float(input(""))

totalExp = bran + trav + food +logi
branpercent = float((bran / totalExp) * 100)
travpercent = float((trav / totalExp) * 100)
foodpercent = float((food / totalExp) * 100)
logipercent = float((logi / totalExp) * 100)


a = f"Total expenses: {totalExp:.2f}"
b = f"Branding expenses percentage: {branpercent:.2f}%"
c = f"Travel expenses percentage: {travpercent:.2f}%"
d = f"Food expenses percentage: {foodpercent:.2f}%"
e = f"Logistic expenses percentage: {logipercent:.2f}%"
print(a)
print(b)
print(c)
print(d)
print(e)