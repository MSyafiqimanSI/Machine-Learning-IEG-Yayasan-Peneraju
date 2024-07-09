def create_summed_set(n, numbers_str):
    numbers_list = list(map(int, numbers_str.split()))

    unique_numbers = sorted(set(numbers_list))

    summed_set = set()

    print(unique_numbers)

    k = int(input())

    for i in range(0, len(unique_numbers), k):
        subset = unique_numbers[i:i+k]
        if len(subset) == k:
            summed_set.add(sum(subset))
        else:
            summed_set.update(subset)

    print(sorted(summed_set))

num = int(input())
string = input()
create_summed_set(num,string)