s = {1,2,3,4,56,6,6,5,5,5,5,5,7,8,9,10}
print(s)
print(type(s))
print(len(s))
# print(s[0]) #sets do not support indexing
# print(s[-1]) #sets do not support indexing

s.add(100)
print(s)
s.add(200)
print(s)
s.remove(3)
print(s)
s.discard(4) #does not raise an error if the element is not found
print(s)
s.pop() #removes and returns an arbitrary element
print(s)
s.pop()
s.pop()
print(s)




print(56 in s)
print(500 in s)
print(500 not in s)
s.clear()
print(s)
print(len(s))

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1|s2)
print(s1.union(s2))
print(s1&s2)
print(s1.intersection(s2))

print(s1 - s2)
print(s1.difference(s2))

print(s2 - s1)
print(s2.difference(s1))
print(s1 ^ s2)
print(s1.symmetric_difference(s2))
print(s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))
s3 = {1,2}
print(s3.issubset(s1))
print(s1.issuperset(s3))
s4 = s1.copy()
print(s4)
s1.clear()
print(s1)
print(s4)

