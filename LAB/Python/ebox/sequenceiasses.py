input1= input()
listinput1 = input1.split(",") # ["1","2","3"]
list_int_1 = set(map(int,listinput1))

input2 = input()
listinput2 = input2.split(",")
list_int_2 = set(map(int,listinput2))

print(list_int_1.issubset(list_int_2))
print(list_int_2.issubset(list_int_2))
print(list_int_1.issuperset(list_int_2))
print(list_int_2.issuperset(list_int_1))

      

