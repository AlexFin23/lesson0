def get_matrix(n, m, value):
    matrix = []
    for row in range (n):
        temp_list = []
        for column in range (m):
            temp_list.append(value)
        matrix.append(temp_list)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)