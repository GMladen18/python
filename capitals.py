countries = input().split(", ")
capitals = input().split(", ")

tuples = list(zip(countries,capitals))
for duos in tuples:
    print(f"{duos[0]} -> {duos[1]}")