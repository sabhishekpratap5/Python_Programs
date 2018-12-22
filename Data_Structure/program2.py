# Write a Python program to reverse the order of the items in the array.

from array import *
num_array = list()
number = int(input("enter number for array: "))
for i in range(number):
    array_num = int(input("enter elements: "))
    num_array.append(array_num)
print(num_array)
num_array.reverse()
print("reversed array is: ")
print(num_array)



