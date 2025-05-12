# How to clone a list without changing the original list in Python
from copy import deepcopy
cool_list = [1, 2, 3, 4, 5]

#print(cool_list)

other_list = cool_list[:]

other_list.append(6)

print(other_list)