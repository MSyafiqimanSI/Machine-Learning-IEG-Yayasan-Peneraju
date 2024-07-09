n = int(input("Enter size of list\n"))
if(n <= 0):print("Invalid input")
else:
    list = []
    print("Enter the elements in list")
    for i in range(n):
        list.append(int(input()))
    print(*filter(lambda x: x % 13 == 0, list))