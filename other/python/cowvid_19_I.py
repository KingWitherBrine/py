def solve(n, stalls):
    max_space = 0
    inserted_zeroes = 0
    for i in range(n):
        if i != 0 and i != n-1:
            if inserted_zeroes != 2 and stalls[i-1] == 0 and stalls[i] == 0 and stalls[i+1] == 0:
                inserted_zeroes += 1
                stalls[i] = 1
    space = 0
    for i in stalls:
        if i != 0:
            space = 0
            continue
        space += 1
        if space > max_space:
            max_space = space
    return max_space

if __name__ == "__main__":
    with open("socdist1.in", "r") as f:
        n = int(f.readline().strip())
        stalls = list(map(int, " ".join(f.readline().strip()).split()))
    with open("socdist1.out", "w") as f:
        f.write(str(solve(n, stalls)))