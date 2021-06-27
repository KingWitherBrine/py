def dot_product(m1, m2):
    m_result = []
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            vec1 = m1[i]
            vec2 = [a[j] for a in m2]
            temp_list = []
            sum_list = [[[0] * len(vec1)] for i in range(len(vec2))]
            for k in range(len(vec1)):
                temp_list.append(vec1[k] * vec2[k])
            temp_sum = sum(temp_list)
            sum_list[i][0][j] = temp_sum
    return sum_list

if __name__ == "__main__":
    A = [[1, 0], [0, 1]]
    B = [[4, 1], [2, 2]]
    print(dot_product(A, B))
