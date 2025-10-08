number = int(input("Number: ")) #asks for a number
product = 1     #the expresion is stated
for i in range(1, number + 1): #does the factorial
    product = product * i
    

print(f"The factorial of  {number} is {product}") #prints the results
