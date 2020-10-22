from collections import defaultdict

heroes_names = input().split(", ")

inventory = defaultdict(list)

while True:

    command = input()
    if command == "End":
        break

    name, item, price = command.split("-")

    if not inventory[name]:
        inventory[name].append(int(price))
        inventory[name].append(1)
        inventory[name].append(item)
    else:
        if item not in inventory[name]:
            inventory[name].append(item)
        else:
            continue
        inventory[name][0] += int(price)
        inventory[name][1] += 1

for name in inventory:
    print(f"{name} -> Items: {inventory[name][1]}, Cost: {inventory[name][0]}")