a=10
b=2.4
c=True
d="Beshwanth Sai Katari"
e=[1,2,3,4,5]
f=(10,20,30,40,50)
g={1,2,3,4,5}
h={ 'name' : 'Beshwanth Sai Katari', 'age' : 21, 'is_student' : True}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(len(d))
print(len(e))
print(len(f))
print(len(g))
print(len(h))
print(e[0])
print(f[0])
print(d[0])
print(h['name'])
print(h['age'])
print(e[::-1])
print(f[::-1])
e.append(6)
print(e)
e.remove(3)
print(e)
h['age'] = 22
print(h)
h['city'] = 'Hyderabad'
print(h)

# This code demonstrates the basic data types in Python including integers, floats, booleans, strings, lists, tuples, sets, and dictionaries. It shows how to create each type, check their types, get their lengths, and perform some basic operations like indexing, slicing, appending to lists, and modifying dictionary entries.
a1=100
b1=200
c=complex(a1,b1)
print(c)
print(type(c))
k=range(1,10)
print(k)
print(type(k))
print(list(k))