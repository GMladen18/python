def line_changing(line):
    new_line = []
    j = 0
    for i in range(len(line)):
        line[i] = line[i][0] + chr(ord(line[i][1]) + j) + line[i][2]
        j += 1
        new_line.append(line[i])
    return new_line


height, width = list(map(int, input().split()))
start = "a" * 3

matrix = [[start for i in range(width)] for _ in range(height)]

#TODO
for i in range(height):
    for j in range(width):
        if i != 0:
            matrix[i][j] = chr(ord(matrix[i][j][0]) + 1) + chr(ord(matrix[i][j][1]) + 1) + chr(ord(matrix[i][j][2]) + 1)
print(matrix)
#
# print((matrix[0]))
# print(line_changing(matrix[0]))
