import random

square_hits = circle_hits = 0
for _ in range(1000000):
    # Generate two random numbers between –1 and 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # The points are always in the square
    square_hits += 1

    # Check whether the point lies in the unit circle
    if x ** 2 + y ** 2 <= 1:
        circle_hits += 1

# The ratio hits / n is approximately the same as the ratio area / square area = pi / 4.
pi = 4 * (circle_hits / square_hits)

print(pi)

