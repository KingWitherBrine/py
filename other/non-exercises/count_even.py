def count_even(seq):
    num_even = 0
    for num in seq:
        if num % 2 == 0:
            num_even += 1
    return num_even
print(count_even([1, 2, 3, 4]))