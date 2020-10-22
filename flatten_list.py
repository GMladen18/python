from itertools import chain

line = input().split("|")
final_list = [[num for num in piece if num != " "] for piece in line[::-1]]

numbers = []

for i in final_list:
    numbers = list(chain(numbers, i))

print(" ".join(numbers))
