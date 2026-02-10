my_set = {1,2,3,3,3,4,5,6,7,8,9}
print(my_set)
#thia saya thst the set will only contains unique eklements and will not contain duplicates. So the output will be {1, 2, 3, 4, 5, 6, 7, 8, 9}

for x in my_set:
    print(x)

my_set.add(2323)
print(my_set)
my_set.add(2323)
print(my_set)
my_set.remove(3)
print(my_set)
my_set.discard(4)
print(my_set)
my_set.update({232,234,235})
print(my_set)
my_set.update([100,200,300])
print(my_set)
my_set.update((400,500,600))
print(my_set)
print(len(my_set))