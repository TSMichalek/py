item1 = input("Item1: ")
item2 = input("Item2: ")
item3 = input("Item3: ")
price1 = float(int(input("Price1: ")))
price2 = float(int(input("Price2: ")))
price3 = float(int(input("Price3: ")))
tax1 = price1 * 0.06
tax2 = price2 * 0.06
tax3 = price3 * 0.06



print(f"{item1} costs ${round(price1, 2)} with tax ${round(tax1, 2)}")
print(f"{item2} costs ${round(price2, 2)} with tax ${round(tax2, 2)}")
print(f"{item3} costs ${round(price3, 2)} with tax ${round(tax3, 2)}")