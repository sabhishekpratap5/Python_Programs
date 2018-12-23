# Write a Python function that takes two lists and returns True if they have at least one common member.


def common_member(list1, list2):
    result = False
    for i in list1:
        for j in list2:
            if i == j:
                result = True
                return result


print(common_member([1,2,3,4,5], [5,6,7,8,9]))
print(common_member([1,2,3,4,5], [6,7,8,9]))