count = int(input("How many numbers? "))
total = 0
for i in range(1, count + 1):
    total += int(input(f"Enter number {i}: "))
average = total / count
print(f"The average is {average}.")

