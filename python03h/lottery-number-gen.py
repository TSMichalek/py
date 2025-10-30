import random
numb = []
value = 0
print("Your lottery numbers:", end=" ")

for i in range(6):
    if value not in numb:
        numb.append(random.randint(1,49))
print(numb)