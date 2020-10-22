rows = int(input())

matrix = [list(map(int, input().split())) for i in range(rows)]

while True:
    command = input()
    if command == "END":
        break

    cmd, row, col, value = command.split()
    if int(row) >= rows - 1 or int(col) >= rows - 1:
        print("Invalid coordinates")
        continue
    if cmd == "Add":
        matrix[int(row)][int(col)] += int(value)
    elif cmd == "Subtract":
        matrix[int(row)][int(col)] -= int(value)

for piece in matrix:
    piece = [str(n) for n in piece]
    print(" ".join(piece))