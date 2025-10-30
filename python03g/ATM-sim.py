balance = 1000
choice = 0
while choice != 4:
    # this will be printed until the user inputs the number 4
    print("ATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Choice: "))

    if choice == 1:
        print(f"Your balance: ${balance}")
    elif choice == 2:
        deposit = int(input("Deposit amount: $"))
        balance = balance + deposit
        print(f"New balance: ${balance}")
    elif choice == 3:
        withdraw = int(input("Withdraw amount: $"))
        balance = balance - withdraw
        print(f"New balance: ${balance}")
print("Thank you for using our ATM!")