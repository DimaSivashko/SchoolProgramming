text = input("Enter text: \n")
letter = input("Enter letter: \n")

words = text.split(" ")

i = 0
for word in words:
    if word[0] == letter:
        i += 1
    else:
        pass

print(i)
