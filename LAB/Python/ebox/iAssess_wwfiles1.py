from collections import Counter

def read_file(filename):
    with open(filename, "r") as file:
        content = file.read().lower()  
        return content

def build_frequency_table(content):
    frequency = Counter(content)
    frequency = {char: count for char, count in frequency.items() if char.isalpha()}
    sorted_frequency = dict(sorted(frequency.items()))
    return sorted_frequency

def print_frequency_table(frequency_table):
    for char, count in frequency_table.items():
        print(f"{char}: {count}")


filename = "frequencyFile.txt"

# filehandler = open(filename, "xt")

content = read_file(filename)

frequency_table = build_frequency_table(content)

print_frequency_table(frequency_table)

