# Write a Python program to convert a list into a nested dictionary of keys.

num_list = [1, 2, 3, 4, 5]
empety_dict = current = {}
for i in num_list:
    current[i]={}
    current = current[i]
print(empety_dict)
