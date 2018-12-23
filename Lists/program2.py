# Write a Python program to multiplies all the items in a list.


def list_multiply(value):
    total = 1
    for i in value:
        total *= i
    return total


print(list_multiply([1, 2, 3, 4]))

