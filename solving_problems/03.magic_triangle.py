def get_magic_triangle(number):
    triangle = [[1 for _ in range(i + 1)] for i in range(number)]

    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if i == 0 or j == 0 or j == len(triangle[i]) - 1:
                continue

            triangle[i][j] += triangle[i - 1][j] + triangle[i - 1][j - 1] - 1

    return triangle


number = int(input())
print(get_magic_triangle(number))
