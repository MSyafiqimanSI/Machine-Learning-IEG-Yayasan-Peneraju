import csv

def readprintcsv(file_name):
    try:
        with open(file_name, mode='r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)  # Read the header row
            print(";".join(headers))  # Print the headers with semicolon
            
            for row in csv_reader:
                print(";".join(row))  # Print each row with semicolon
                
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File name
file_name = 'SalariesDataSet.csv'

# Call the function to read and print the CSV file
readprintcsv(file_name)
