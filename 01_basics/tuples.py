## tuples are faster compared to lists
## tuples are immutable (cannot be changed after creation)
# Creating a tuple

tup = (1,2,3,4,500,6,7,8,9,10)
print(tup)
print(type(tup))
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2:8])
print(tup[::-1])
print(tup[:])
print(tup[1:10:2])
# # tup[0] = 99 # This will raise an error because tuples are immutable
# print(tup)
#
# #tuple object does not support item assignment
# # tup[0]=  99
# print(tup)
print(tup.index(500))
print(tup.count(9))