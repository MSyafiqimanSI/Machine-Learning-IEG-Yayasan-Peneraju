def file_number_line(filename):
    with open (filename, "r") as file:
        lines = file.readlines()
        linecount = len(lines)
        print(f"The file has {linecount} lines")
        
            
filename = "input.txt"
file_number_line("input.txt")
