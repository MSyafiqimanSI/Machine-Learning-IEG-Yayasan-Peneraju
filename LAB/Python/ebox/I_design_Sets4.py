def update_dict(n,dict):
    name, *marks = n.split()
    dict[name] = [int(mark) for mark in marks]

def second_highest(key, dict):
    marks = dict[key]
    if all(mark == marks[0] for mark in marks): 
        print(f"{key} scored same marks in all subjects: {marks[0]}")
    else:
        highest = max(marks)
        marks = [mark for mark in marks if mark != highest] 
        second_highest = max(marks)
        print(f"Second Highest mark of {key}: {second_highest}")

def main(m):
    dict = {}
    for i in range(m):
        name = input()
        update_dict(name, dict)
    key = input()
    if key in dict:
        second_highest(key,dict)
    else:
        print("Student doesn't exist")
n = int(input())
main(n)