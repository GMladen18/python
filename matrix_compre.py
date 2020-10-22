nums_matr = int(input())
matrix = [(list(map(int, input().split(", ")))) for _ in range(nums_matr)]

for n in range(len(matrix)):
    for i in matrix[n].copy():
        if i % 2 != 0:
            matrix[n].remove(i)


print(matrix)

