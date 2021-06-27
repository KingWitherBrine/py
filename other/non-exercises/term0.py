import math

def term0(num):
    count = 0
    num_str = str(num)
    for i in range(len(num_str)):
        if num_str[-i - 1] == '0':
            count += 1
        else:
            break
    return count

n = math.factorial(101)
print(term0(n))