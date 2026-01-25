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

