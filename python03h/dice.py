import random

rolls = int(input("How many rolls of the die? "))
counter = 0

for i in range(1, rolls + 1):
    roll = random.randint(1, 6)
    counter += roll
    print(f"Die {i}: {roll}")
    
average = counter / rolls
print(f"Average roll: {average}")


