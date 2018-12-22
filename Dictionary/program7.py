# Write a Python program to print all unique values in a dictionary.
# 	Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
# 	{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

L = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},{"VIII": "S007"}]
print("original List: ", L)

unique_value = set(value for dic in L for value in dic.values())
print("unique value: ", unique_value)
