# Write a Python program to check multiple keys exists in a dictionary.

student = {'name': 'abc',
           'class': 'V',
           'roll_no': '1'}

print(student.keys() >= {'name', 'class'})
print(student.keys() >= {'class', '2'})
print(student.keys() >= {'roll_no', 'name'})
