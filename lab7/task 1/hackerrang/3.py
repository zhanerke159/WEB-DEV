n = int(input())

students = []

for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])
grades = [student[1] for student in students]
unique_grades = sorted(set(grades))
second_lowest = unique_grades[1]
names = [student[0] for student in students if student[1] == second_lowest]
names.sort()

for name in names:
    print(name)