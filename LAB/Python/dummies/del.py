bs = int(input())
hra1 = 0.15
hra2 = 5000
da1 = 0.9
da2 = 0.98

if bs < 15000:
    gs = bs + (hra1*bs) + (da1*bs)
    print(f"{gs:.2f}")
else:
    gs = bs + hra2 + (da2*bs)
    print(f"{gs:.2f}")
