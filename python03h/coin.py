import random

print("Flipping a coin 20 times...")
heads = 0
tails = 0
for i in range(20):
    side = random.randint(0,1)
    if side == 0:
        print("H", end=" ")
        heads += 1
    else:
        print("T", end=" ")
        tails += 1
print()
print(f"Heads {heads}")
print(f"Tails {tails}")