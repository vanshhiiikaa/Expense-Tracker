import numpy as np

marks = []
for mark in range(5):
    marks.append(int(input(f"Enter mark for student {mark + 1}: ")))

print("Marks:", marks)

print("Total Marks:", np.sum(marks))
print("Average Mark:", np.mean(marks))
print("Maximum Mark:", np.max(marks))
print("Minimum Mark:", np.min(marks))

percentage = (np.sum(marks) / (len(marks) * 100)) * 100
print("Percentage:", percentage, "%")

average = np.mean(marks)
if average >= 90:
    grade = 'A+' 
elif average >= 80:
    grade = 'A'
elif average >= 70:
    grade = 'B'
else:
    grade = 'C'

print("Grade:", grade)