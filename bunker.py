materials = {x: [] for x in input().split(", ")}
n = int(input())
quantity = 0
quality = 0
for i in range(n):
    line = input().split(" - ")
    materials[line[0]].append(line[1])
    quantity += int((line[2].split(";")[0]).split(":")[1])
    quality += int((line[2].split(";")[1]).split(":")[1])

print(f"Count of items: {quantity}")
print(f"Average quality: {(quality / len(materials)):.2f}")

for material in materials:
    print(f"{material} -> {', '.join(materials[material])}")