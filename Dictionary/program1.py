# Write a Python script to sort (ascending and descending) a dictionary by value

import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(sorted(d.items(), key=operator.itemgetter(0)))
