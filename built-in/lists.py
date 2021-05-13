# empty list
list1 = []
print(list1)
# homogenous list

list2 = [1, 2, 3, 'bikotest']
print(list2)

#llist functions for adding data in a list: append(), extend() & insert()
list1.append(5)
print(list1)
list1.append((1, 0))
print(list1)

list2.append(10)
print(list2)

list1.extend((5, 9))
print(list1)

list2.extend((4, 5))
print(list2)

list1.insert(2, 'Git it good')
print(list1)

list2.insert(3, 'Git It Best')
print(list2)

#deleting data from list: del, pop(), remove():

del list1[2]
print(list1)

del list2[3:5]
print(list2)

a = list1.pop(2)
print(a)

b = list2.pop(3)
print(b)

list1.remove(5)
print(list1)

list2.remove(3)
print(list2)

#accessing full list
print(list1)
print(list2)

#accessing particular elements
print(list1[0:2])
print(list2[2:3])

#skipping elements
print(list1[0:2:2])


#reverse order of list
print(list1[::-1])
print(list2[::-1])

a = 'steve'
print(a[::-1])

list3 = [1, 2, 3, 54, 10, 34 , 48, 0]
print(list3)
print(sorted(list3))

#changing the actual order of list:
list3.sort(reverse=True)
print(list3)

#finding index of an element:
print(list3.index(48))

#finding count of a specific value:
print(list3.count(2))