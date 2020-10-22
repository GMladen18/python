word = input()

new_word = "".join([i for i in word if i != "a" and i != "o" and i != "u" and i != "e" and i != "i" \
                    and i != "A" and i != "O" and i != "U" and i != "E" and i != "I"])
print(new_word)