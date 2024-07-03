x = int(input("Enter the number of clients\n"))
data_dict = {}
passportList = []
for i in range (0,x):
    print(f'Enter the details of the client {i+1}\n')
    name = input()
    email = input()
    passport_no=int(input())
    # passportList.append((passport_no,name,email))
    data_dict[passport_no] = f"{name}--{email}--{passport_no}"
# print(passportList)

# print(passportList)

# for item in passportList:
#     key = item[0]
#     values = item[1:2]
#     data_dict[key] = values

# print(data_dict)

searchNo = int(input("Enter the passport number of the client to be searched\n"))

if searchNo in data_dict:
    print("Client Details")
    print(data_dict[searchNo])

else:
    print("Client not found")