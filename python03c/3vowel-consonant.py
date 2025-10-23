vowels = 0
consonants = 0

text = input("Enter text: ")

for char in text:
        if char in "aeiouAEIOU":
            vowels += 1
        if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            consonants += 1
            
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
        

