number = int(input("Enter a number: "))
output = 0
for i in range(1, number + 1, 2):
    output = output + i
print(f"The sum of odd numbers from 1 to {number} is {output}.")