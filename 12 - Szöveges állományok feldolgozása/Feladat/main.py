from typing import *
from student import Student 
from studentIO import importStudents

students: List[Student] = importStudents()
print(students)

for student in students:
    print(student)