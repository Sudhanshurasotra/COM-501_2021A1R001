def reverse_kth_rows(matrix, k):
    if k <= 0:
        print("Invalid value of k")
        return

    for i in range(0, len(matrix), k):
        matrix[i:i+k] = matrix[i:i+k][::-1]

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
k = 2  # Reverse every 2nd row

reverse_kth_rows(matrix, k)

for row in matrix:
    print(row)