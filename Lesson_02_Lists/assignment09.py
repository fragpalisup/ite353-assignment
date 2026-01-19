def transpose_matrix(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

original = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = transpose_matrix(original)

print("Original matrix:")
for row in original:
    print(row)

print("\nTransposed matrix:")
for row in transposed:
    print(row)
