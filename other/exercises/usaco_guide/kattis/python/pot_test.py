def digit_one_by_one(num):
    if num == 0:
        return [0]
    results = []
    while num != 0:
        results.append(num % 10)
        num //= 10
    # results.reverse()
    return results[::-1]

print(digit_one_by_one(int(input())))