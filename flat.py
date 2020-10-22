n = int(input())
matrix = [list(map(int, input().split(", "))) for _ in range(n)]

flat_matrix = []
for i in range(len(matrix)):
    for num in matrix[i]:
        flat_matrix.append(num)

print(flat_matrix)
