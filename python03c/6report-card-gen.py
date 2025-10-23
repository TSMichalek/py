name = str(input("Name: "))
subjects = []
grades = []

for i in range(1, 6):
    subject = str(input("Subject: "))
    grade = int(input("Grade: "))
    subjects.append(subject)
    grades.append(grade)

for j in range(5):
    print(subjects[j], "grade is", grades[j])

average_grades = sum(grades) / 5

if average_grades >= 90:
    print("Letter grade: A")
elif average_grades >= 80:
    print("Letter grade: B")
elif average_grades >= 70:
    print("Letter grade: C")
elif average_grades >= 60:
    print("Letter grade: D")
elif average_grades >= 50:
    print("Letter grade: F")

