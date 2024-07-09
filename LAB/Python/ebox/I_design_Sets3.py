def Updatedict(n,dict):
    name, *marks = n.split()
    dict[name] = [int(mark) for mark in marks]

def Calculateavg(key,dict):
    marks = dict[key]
    avg = sum(marks)/len(marks)
    print(f"Average Mark of is : {avg:.2f}")

def main(m):
    dict = {}
    for i in range(m):
        name = input()
        Updatedict(name, dict)
    key = input()
    Calculateavg(key,dict)

n = int(input())
main(n)