# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# 	Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# 	Expected Output : ['Green', 'White', 'Black']


sample_list= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

del sample_list[0]
del sample_list[2]
del sample_list[3]
print(sample_list)

# or
sample_list1= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
sample_list1 = [index for (i, index) in enumerate(sample_list1) if i not in (0, 4, 5)]
print(sample_list1)
