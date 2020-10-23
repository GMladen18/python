def find_player(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "P":
                return i, j


def move(matrix, player_position, direction):
    i, j = player_position
    letter = ""
    is_punished = False
    if direction == "right":
        if j + 1 < len(matrix[i]):
            letter = matrix[i][j + 1]
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
            if letter != "-":
                matrix[i][j] = "-"
        else:
            is_punished = True

    elif direction == "left":
        if j - 1 >= 0:
            letter = matrix[i][j - 1]
            matrix[i][j], matrix[i][j - 1] = matrix[i][j - 1], matrix[i][j]
            if letter != "-":
                matrix[i][j] = "-"
        else:
            is_punished = True

    elif direction == "up":
        if i - 1 >= 0:
            letter = matrix[i - 1][j]
            matrix[i][j], matrix[i - 1][j] = matrix[i - 1][j], matrix[i][j]
            if letter != "-":
                matrix[i][j] = "-"
        else:
            is_punished = True

    elif direction == "down":
        if i + 1 < len(matrix):
            letter = matrix[i + 1][j]
            matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
            if letter != "-":
                matrix[i][j] = "-"
        else:
            is_punished = True
    return matrix, letter, is_punished


word = input()
height = int(input())
field = [list(input()) for _ in range(height)]
iterations = int(input())

for _ in range(iterations):
    direction = input()
    player_position = find_player(field)
    field, letter, is_punished = move(field, player_position, direction)
    if is_punished:
        word = word[:-1]
        continue
    if letter != "-":
        word += letter

print(word)
for row in field:
    print("".join(row))
