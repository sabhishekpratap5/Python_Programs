# Write a Python program to count the number of strings where the string length is 2 or more and
# the first and last character are same from a given list of strings.
# 	Sample List : ['abc', 'xyz', 'aba', '1221']
# 	Expected Result : 2


def num_string(word_list):
    count = 0
    for i in word_list:
        if len(i) > 1 and i[0] == i[-1]:
            count += 1
    return count


print(num_string(['abc', 'xyz', 'aba', '1221']))