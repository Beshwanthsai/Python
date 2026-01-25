d = {1:2,2:3}
print(d)
print(type(d))
print(len(d))

print(d[1])
print(d[2])

d1 = {'name' : 'Beshwanth Sai Katari', 'age' : 21, 'is_student' : True}
print(d1)
print(type(d1))
print(len(d1))
print(d1['name'])
print(d1['age'])
print(d1['is_student'])
d1['age'] = 22
print(d1)
d1['is_student'] = False
print(d1)
d1['city'] = 'Hyderabad'
print(d1)
del d1['city']
print(d1)
d1['city'] = 'bangalore'
d1['company'] = 'Google'
print(d1)
print(d1.keys())
print(d1.values())
print(d1.items())
for key in d1:
    print(key, ":", d1[key])
