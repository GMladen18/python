words = input().split(", ")

name_dict = {word: len(word) for word in words}
counter = 1
for name in name_dict:
    if counter < len(name_dict):
        print(f"{name} -> {name_dict[name]}", end=", ")
        counter += 1
    else:
        print(f"{name} -> {name_dict[name]}")
