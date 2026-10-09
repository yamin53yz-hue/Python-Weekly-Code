from grade import get_grade

name = input("Enter student name: ")
score = int(input("Enter score: "))

grade = get_grade(score)

print("Name:", name)
print("Score:", score)
print("Grade:", grade)