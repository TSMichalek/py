text = input("Enter some text: ")
leta = 0

for i in text:
    if i in "aA":
        leta += 1

print(f"The letter 'a' appears {leta} times")