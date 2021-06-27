from itertools import permutations

def solve():
    perms = permutations(range(10))

    for (i, n, r, c, s, o, v, u, g, a) in perms:
        if r + 1 == c:
            rising = g + n * 10 + i * 10**2 + s * 10**3 + i * 10**4 + r * 10**5
            virus = s + u * 10 + r * 10**2 + i * 10**3 + v * 10**4
            corona = a + n * 10 + o * 10**2 + r * 10**3 + o * 10**4 + c * 10**5
            if rising + virus == corona:
                return (rising, virus, corona)
        
if __name__ == "__main__":
    print(*solve())