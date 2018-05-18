userinput = input("Please type words: ")
answer = ""
excluded = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
for letter in userinput:
    if letter not in excluded:
        answer = answer + letter

print(answer)