# Write a Python program to sum all the items in a list.


def list_sum(value):
    sum_val = 0
    for i in value:
        sum_val += i
    return sum_val


print(list_sum([1, 2, 3, 4]))
