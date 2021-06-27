def solve(matrix):
    count = 0
    for i in matrix:
        count += int(str(i)[0:-1]) ** int(str(i)[-1])
    return count

if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        matrix = [int(f.readline()) for i in range(n)]
    print(solve(matrix))