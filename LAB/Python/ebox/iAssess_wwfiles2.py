def read_input():
    n = int(input("Enter the number of persons: "))
    data = []
    for _ in range(n):
        name = input("Enter the name: ")
        salary = input("Enter the salary: ")
        data.append((name, salary))
    return data

def write_to_csv(data, filename):
    with open(filename, 'w') as file:
        for name, salary in data:
            file.write(f"{name},{salary}\n")

def print_file_content(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

def main():
    data = read_input()
    filename = "salaryData.csv"
    write_to_csv(data, filename)
    print_file_content(filename)

if __name__ == "__main__":
    main()