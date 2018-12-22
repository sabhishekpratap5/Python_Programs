# Write a Python program to get the number of occurrences of a specified element in an array

from array import *
num_array = list()
num = int(input("how many element you want enter in the array: "))
for i in range(num):
    array_num = int(input("enter element: "))
    num_array.append(array_num)
print("enterd array is: ")
print(num_array)

n = int(input("enter number for checking occurrence: "))
print(num_array.count(n))
