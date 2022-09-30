## here happialy exam marks calculate
from unicodedata import name


print("enter your name")
name_student = input()
print("your name is:",name_student)

print("exam obtained marks of MATH ")
MATH = int(input())
print("exam obtainer marks of PHYSICS : " )
PHYSICS = int(input())
print("exam obtained marks of ENGLISH")
ENGLISH = int(input())

aaa = float(input())

avg = MATH + ENGLISH + PHYSICS + aaa / 3
print("your avg score is :",avg)

