def solve(cow_name, matrix):
    x_vals, y_vals = {}, {}
    for i in range(len(matrix)):
        x_vals[i] = i[0]
        y_vals[i] = i[1]
    min_x, min_y, max_x, max_y = [0], [0], [0], [0]
    for i in x_vals:
        if x_vals[i] <= min_x[i-1]:
            min_x.append(matrix[i])
        if x_vals[i] >= max_x[i-1]:
            max_x.append(matrix[i])
        if y_vals[i] <= min_y[i-1]:
            min_y.append(matrix[i])
        if y_vals[i] >= max_y[i-1]:
            max_y.append(matrix[i])
    min_x_min, min_x_max, min_y_min, min_y_max, max_x_min, max_x_max, max_y_min, max_y_max  = 0
    min_x_min = [i for i in min_x if i[0] < min_x_min]
    for i in min_x:
        if i[0] < min_x_min:
            min_x_min = i
    for i in min_x:
        if i[0] > min_x_max:
            min_x_max = i

    for i in max_x:
        if i[0] < max_x_min:
            max_x_min = i
    for i in max_x:
        if i[0] > max_x_max:
            max_x_max = i

    for i in min_y:
        if i[0] < min_y_min:
            min_y_min = i
    for i in min_y:
        if i[0] > min_y_max:
            min_y_max = i

    for i in max_y:
        if i[0] < min_x_min:
            max_y_min = i
    for i in max_y:
        if i[0] > min_x_max:
            max_y_max = i

    
if __name__ == "__main__":
    with open(0) as f:
        cow_num = int(f.readline().strip())
        matrix = [list(map(int, f.readline().strip().split())) for i in range(cow_num)]
    print(solve(cow_num, matrix))