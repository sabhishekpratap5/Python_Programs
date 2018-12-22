# Write a Python program to print a dictionary in table format.

tabel_formate = {'c1': [1, 2, 3], 'c2': [4, 5, 6], 'c3': [7, 8, 9]}
for row in zip(*([key] + value for key, value in sorted(tabel_formate.items()))):
    print(*row)
