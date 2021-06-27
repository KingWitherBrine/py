def solve(cow_num, matrix):
    counts = []
    min_x, min_y, max_x, max_y = min(matrix), min(matrix, key=lambda p: p[1]), max(matrix), max(matrix, key=lambda p: p[1])
    items = [min_x, min_y, max_x, max_y]
    for i in items:
        new_matrix = matrix[:]
        new_matrix.pop(matrix.index(i))
        new_min_x = min(new_matrix)
        new_min_y = min(new_matrix, key=lambda p: p[1])
        new_max_x = max(new_matrix)
        new_max_y = max(new_matrix, key=lambda p: p[1])
        counts.append((new_max_x[0] - new_min_x[0]) * (new_max_y[1] - new_min_y[1]))
    return min(counts)

if __name__ == "__main__":
    with open(0) as f:
        cow_num = int(f.readline().strip())
        matrix = [list(map(int, f.readline().strip().split())) for i in range(cow_num)]
    print(solve(cow_num, matrix))

#  Creator: Noah Chen
#  Copyright 2020 Noah Chen Corporation