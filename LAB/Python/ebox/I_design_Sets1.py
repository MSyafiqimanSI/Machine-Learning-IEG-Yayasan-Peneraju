n = int(input())

uniquelist = []
for _ in range(n):
    a, *b = map(int, input().split(','))
    uniquelist.extend([a, *b])

uniquelist = list(set(uniquelist))  # Convert set to list
uniquelist.sort()
print(f"set({uniquelist})")
print(uniquelist[-2])