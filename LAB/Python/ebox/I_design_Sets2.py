def check_in_dict(n):
    dict = {}
    for i in sorted(n):
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(f"Dictionary of string: {dict}")
    return dict

def print_char(c):
    for i in sorted(c):
        print(f"{i}--{c[i]}")

n = input()
dict = check_in_dict(n)
print_char(dict)