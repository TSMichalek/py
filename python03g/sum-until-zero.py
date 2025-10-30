total = 0

while True:
    # if the user inputs "0" then the loop will stop and add up all of the other numbers the user has typed
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    total += number
print(f"Total sum: {total}")