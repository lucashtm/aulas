students = [
  ['Jorge', 26],
  ['Lucas', 27],
  ['Yuri', 28, 'O+']
]

student = students[2]

name = student[0]
age = student[1]
blood_type = ''

if len(student) > 2:
  blood_type = student[2]

print(name, age, blood_type)
