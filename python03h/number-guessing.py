import random

secret = random.randint(1, 100)

guesses = 0

print("Think of a number between 1 and 100...")
while True:
    # this will loop forever until the user input the random number
    guesses += 1
    guess = int(input("My guess is "))
    if guess > secret:
        print("Too high.")
    elif guess < secret:
        print("Too low.")
    elif guess == secret:
        print(f"I got it in {guesses} guesses!")