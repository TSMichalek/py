import random

secret = random.randint(1, 50)

guesses = 0

print("I'm thinking of a number between 1 and 50...")
while True:
    # this will loop forever until the user input the random number
    guesses += 1
    guess = int(input("Your guess: "))
    if guess > secret:
        print("Too high.")
    elif guess < secret:
        print("Too low.")
    elif guess == secret:
        print(f"Correct! You got in {guesses} guesses!")
    