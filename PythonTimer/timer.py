import time
from copy import  deepcopy


my_list = [1, 2, 3, 4, 5]

start = time.time()
new_list =  my_list[:]
new_list =  my_list[:]
new_list =  my_list[:]
new_list =  my_list[:]
new_list =  my_list[:]
end = time.time()
length = end   - start
print(length)

start1 = time.time()
new_list2 = deepcopy(my_list)
new_list2 = deepcopy(my_list)
new_list2 = deepcopy(my_list)
new_list2 = deepcopy(my_list)
new_list2 = deepcopy(my_list)
end1 = time.time()
length1 = end1   - start1

print(length1)