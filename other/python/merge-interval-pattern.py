def merge_interval(matrix):
    matrix = sorted(matrix)
    output = []
    temp_tup = matrix[0]
    for i in range(len(matrix)):
        if matrix[i][0] > temp_tup[1]:
            output.append(temp_tup)
            temp_tup = matrix[i]
        else:
            temp_tup[1] = max(temp_tup[1], matrix[i][1])
    output.append(temp_tup)
    return output

if __name__ == "__main__":
    with open(0) as f:
        # matrix = [[1, 5], [2, 7], [6, 12], [34, 39]]
        # matrix = [[1, 3], [2, 6], [8, 10], [15, 18]]
        # matrix = [[1, 6], [2, 3], [4, 10], [13, 15], [14, 17]]
        # matrix = [[2, 3], [3, 5], [4, 7], [9, 10]]
        # matrix = [[1, 3], [2, 5], [3, 4]]
        # matrix = [[1, 9], [2, 3], [7, 10], [4, 5], [27, 30], [28, 29]]
        # matrix = [[1, 9], [2, 3], [7, 10], [4, 5]]
        matrix = [[1, 3], [2, 4], [6, 8], [9, 10]]
    print(merge_interval(matrix))