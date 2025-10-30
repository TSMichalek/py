average = 0

while True:
    # this will loop forever until the user input "-1"
    number = int(input("Enter a number (-1 to finish): "))
    if number == -1:
        break
    average += number
print(f"Average: {average}")