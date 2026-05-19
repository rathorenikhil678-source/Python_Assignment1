# Student Result with Grade

name = input("Enter student name: ")
student_class = input("Enter class: ")


sub1 = int(input("Enter marks of Subject 1: "))
sub2 = int(input("Enter marks of Subject 2: "))
sub3 = int(input("Enter marks of Subject 3: "))
sub4 = int(input("Enter marks of Subject 4: "))
sub5 = int(input("Enter marks of Subject 5: "))


total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5


if percentage >= 60:
    grade = "A"
elif percentage >= 50 and percentage < 60:
    grade = "B"
elif percentage >= 40 and percentage < 50:
    grade = "C"
elif percentage >= 33 and percentage < 40:
    grade = "D"
else:
    grade = "Fail"


print("\n----- Student Result -----")
print("Name:", name)
print("Class:", student_class)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)