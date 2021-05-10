dict1 = {1: 'Vue', 2: 'Vue.js'}
print(dict1)

#changing value in a dictionary

dict1[1]='Django'
print(dict1)

#adding anew value
dict1[3] = 'Pyhton'
print(dict1)

#deleting elements

del dict1[1]
print(dict1)

print(dict1.pop(1))
print(dict1)

print(dict1.popitem())

#getting all the keys & values
print(dict1.keys())
print(dict1.values())

#getting the items(keys & values)
print(dict1.items())