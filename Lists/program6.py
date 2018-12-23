# Write a Python program to remove duplicates from a list.

list1 = [1, 2, 3, 4, 1, 3, 5, 6, 7, 6, 5, 10, 2, 2]

duplicates = set()
unique_value = []
for i in list1:
    if i not in duplicates:
        unique_value.append(i)
        duplicates.add(i)

print(duplicates)
print(unique_value)
