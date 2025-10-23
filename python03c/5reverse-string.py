string = input("Enter a word: ")
reversed_str = ""

for char in string:
    reversed_str = char + reversed_str
print(reversed_str)