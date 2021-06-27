import math

number = 2**1234 - 1

sqrt_number = math.ceil(math.sqrt(number))

is_prime = True

for i in range(2, sqrt_number + 1):
    if number % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"This is not a prime number, because {number} is divisible by {i} and {number // i}")