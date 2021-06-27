def transpose(m):
    x, y = len(m), len(m[0])
    m_t = [[0] * x for i in range(y)]
    for i in range(len(m)):
        for j in range(len(m[i])):
            m_t[j][i] = m[i][j]

    return m_t
print(transpose([[-1], [-1]]))