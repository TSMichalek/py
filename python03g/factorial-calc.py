number = int(input("Enter a number: "))
product = 1
count = 1

while count <= number:
    # this will continue until the number of times it loops equals the inputed number
    product = count * product
    count += 1

print(f"{number}! = {product}")