
def sum_of_all_values(filename):
    total_sum = 0  
    with open(filename, 'r') as file:
        text = file.read()  
        words = text.split()  

        for word in words:
            if word.isdigit():  
                total_sum += int(word)  

    return f"The sum of the integers in the file sample.txt is:{total_sum}" 

print(sum_of_all_values("sample.txt"))
