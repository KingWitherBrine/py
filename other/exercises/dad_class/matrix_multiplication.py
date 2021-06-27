def dot_product(m1, m2):
    m, n = len(m1), len(m1[0])
    o, p = len(m2), len(m2[0])
    if n != o:
        return
    res = [[0] * p for _ in range(m)]
    
    for i in range(m):
        for j in range(p):
            for k in range(n):
                res[i][j] += m1[i][k] * m2[k][j]
    return res


def dot_product2(m1, m2):
    m_final = []
    for i in m1:
        m_final.append(dp_1_n(i, m2))
    return m_final

def dp_1_1(m1, m2):
    m_result = 0 
    for i in range(len(m1)):
        m_result += m1[i] * m2[i]
    return m_result

def dp_1_n(m1, m2): # O(n^2)
    m_list = []
    for i in range(len(m2[0])):
        vec1 = m1
        vec2 = [vec[i] for vec in m2]
        m_list.append(dp_1_1(vec1, vec2))
    return(m_list)

if __name__== '__main__':
    A2 = [[1, 2, 1], [4, 5, 1]]
    B2 = [[4, 1], [2, 2], [7, 8]]

    print(dot_product(A2, B2))
    print(dot_product2(A2, B2))

    # A2 = [[2, 1], 
    #       [2, 2]]
    # B2 = [[1, 0], 
    #       [1, 1]]
    # print(dot_product(A2, B2))

    # A2 = [[1, 2, 3], [4, 5, 6]]
    # B2 = [[4, 1], [2, 2], [7, 8]]
    # print(dot_product(A2, B2))

    