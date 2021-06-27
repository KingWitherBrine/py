nums = [1, 2, 3, 4, 5, -89, 194, 9, 7, 6]
total = 0
for i, e in enumerate(nums):
    if i % 2 == 1:
        total += e
print(total)