def calculate_average_word_length(filename):
    with open(filename, 'r') as file:
        text = file.read()

    words = text.split()

    total_length = sum(len(word) for word in words)

    num_words = len(words)

    average_length = total_length / num_words if num_words > 0 else 0

    print(int(average_length))

calculate_average_word_length('averageLength.txt')
