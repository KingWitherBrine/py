def solve(n, matrix):
    d = dict(matrix)
    r = 10 ** 6 + 1
    for i in d:
        for j in d:
            if d[i] != d[j]:
                if abs(i-j) < r:
                    r = abs(i-j)
    count = 0
    for i in d:
        for j in d:
            if d[i] == 1 and d[j] == 1 and i != j:
                if abs(j-i) <= r:
                    count += 1
    return count//2
if __name__ == "__main__":
    with open("socdist2.in", "r") as f:
        n = int(f.readline().strip())
        matrix = sorted([list(map(int, f.readline().strip().split())) for i in range(n)])
    with open("socdist2.out", "w") as f:
        f.write(str(solve(n, matrix)))