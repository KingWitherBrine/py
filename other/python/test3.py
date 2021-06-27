def solve_time(removing_start, removing_end, matrix):
    matrix = matrix[:]
    time = 0
    matrix.remove([removing_start, removing_end])
    previous_s, previous_e = matrix[0][0], matrix[0][1]
    for i in range(1, len(matrix)):
        if previous_s < matrix[i][0] < previous_e:
            previous_e = max(previous_e, matrix[i][1])
        else:
            time += previous_e - previous_s
            previous_s, previous_e = matrix[i][0], matrix[i][1]
    time += previous_e - previous_s
    return time
def solve(matrix):
    matrix = sorted(matrix)
    times = [solve_time(removing_start, removing_end, matrix) for removing_start, removing_end in matrix]
    max_time = max(times)
    return max_time

if __name__ == "__main__":
    with open("lifeguards.in", "r") as f:
        n = int(f.readline().strip())
        matrix = [list(map(int, f.readline().strip().split())) for i in range(n)]
    with open("lifeguards.out", "w") as f:
        f.write(str(solve(matrix)))