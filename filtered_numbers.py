start_index = int(input())
end_index = int(input())
filtered_numbers = [
    {n for n in range(start_index, end_index + 1) if n % m == 0}
    for m in range(2, 11)

]
s = set()
for i in range(len(filtered_numbers)):
    if not filtered_numbers[i]:
        continue
    s = s.union(filtered_numbers[i])



print(list(s))