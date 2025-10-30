while True:
    grade = int(input("Enter a grade (0-100): "))
    if grade <= 0 or grade >= 100:
        # the program will continue to print this message if the user doesn't input a number that's in between 0 and 100
        print("Invalid! Must be between 0 and 100.")
    else:
        print(f"Valid grade accepted: {grade}")
        break
