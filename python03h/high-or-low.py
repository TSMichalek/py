import random
win = 0
lose = 0

while True:
    number = random.randint(1,100)
    print(f"Current number: {number}")
    next_number = random.randint(1,100)
    answer = str(input("Will the next number be (h)igher or (l)ower? "))
    if answer == "h":
        if next_number > number:
            print("You win!")
            print(f"Next number: {next_number}")
            win += 1
        else:
            print(f"Next number: {next_number}")
            print("You lose!")
            lose += 1
            break
    if answer == "l":
        if next_number < number:
            print("You win!")
            print(f"Next number: {next_number}")
            win += 1
        else:
            print("You lose!")
            print(f"Next number: {next_number}")
            lose += 1
            break
print(f"Score: {win} wins, {lose} loss")
