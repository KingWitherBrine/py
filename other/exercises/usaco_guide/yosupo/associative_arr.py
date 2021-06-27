def solve(n, matrix):
    d = {}
    results = []
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            k = matrix[i][1]
            d[k] = matrix[i][2]
        if matrix[i][0] == 1:
            results.append(d.get(matrix[i][1], 0))
    return results

if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline())
        matrix = [list(map(int, f.readline().strip().split())) for i in range(n)]
    for i in solve(n, matrix):
        print(i)