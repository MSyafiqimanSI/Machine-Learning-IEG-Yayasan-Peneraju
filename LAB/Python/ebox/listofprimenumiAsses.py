a = int(input())
b = int(input())

for num in range(a, b + 1):
    is_prime = True
    if num < 2:
        is_prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
    if is_prime:
        print(num, end=" ")

print()
