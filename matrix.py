def get_diagonal(matrix):
    diagonal = 0
    nums = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == i:
                diagonal += matrix[i][j]
                nums.append(str(matrix[i][j]))
    numbers = (diagonal, nums)
    return numbers


def rotated(matrix):
    list_of_tuples = zip(*matrix[::-1])
    return [list(elem) for elem in list_of_tuples]


n = int(input())
matrix = [list(map(int, input().split(", "))) for i in range(n)]
rotated_matrix = rotated(matrix)

print(f"First diagonal: {', '.join(get_diagonal(matrix)[1])}. Sum: {get_diagonal(matrix)[0]}")
print(f"Second diagonal: {', '.join(get_diagonal(rotated_matrix)[1])}. Sum: {get_diagonal(rotated_matrix)[0]}")