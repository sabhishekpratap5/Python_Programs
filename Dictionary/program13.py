# Write a Python program to count number of items in a dictionary value that is a list.

dict1 = {'value1': ['num1', 'num2'], 'value2': ['num3', 'num4', 'num5']}
num_key = sum(map(len,dict1.values()))
print(num_key)
