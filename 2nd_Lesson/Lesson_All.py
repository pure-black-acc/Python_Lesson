# List
# List is a command which stores the lists of data which can be edit, delete, and added
# Ex)
# a = []
# b = [1,2,3]
# c = ['life is too short', 'use python']
# d = [1, 2, 'life is too short', 'use python']
# e = [1, 2, ['life is too short', 'use python']]

# List - Indexing
# Indexing is what you call when you approach the data of a certain list with a number that shows the cordinates of that data
# Ex)
a = [1,2,3,4]
print(f"a[0] : {a[0]}")
print(f"a[-1] : {a[-1]}")

a = [1,2,3,['a','b','c']]
print(f"a[0] : {a[0]}")
print(f"a[-1] : {a[-1]}")
print(f"a[-1][0] : {a[-1][0]}")

# F-string, you can print variables with this
# print(f"{Variable}")
i = 10
print(f"i : {i}")

# List slicing
# List slicing is a feature which extract the formal list(only part of it) and make a new list
a = [1,2,3,4,5]
print(f"a[1:4] : {a[1:4]}")
a = [1,2,3,4,5]
print(f"a[:3] : {a[:3]}")
print(f"a[3:] : {a[3:]}")

# List Calulate
# i wont write much on here(it's just too simple)

# 1 - Addition
a = [1,2,3]
b = [4,5,6]
print(f"a+b = {a+b}")

# 2 - List loop
a = [1,2,3]
print(f"a*2 = {a*2}")

# 3 - List Length
# 'len' is a command that tells the length if the list
a = [1,2,3]
print(f"len(a) : {len(a)}")

# List Edit
# like above one, I wont say much

# 1 - Edit
a = [1,2,3]
a[2] = 4
print(f"{a}")

# 2 - delete
a = [1,2,3]
del a[1]
print(f"{a}")

# 3 - delete(slicing.ver)
a = [1,2,3,4,5]
del a[2:]
print(f"{a}")

# List functions
# Yeah, it's like above ones, imma just write one by one

# 1 - append(like adding contents)
a = [1,2,3] 
a.append(4)
b = [4,5,6]
a.append([1,2])
print(f"{a}")
print(f"{b}")

# 2 - sort(sorting, yk right?)
a = [3,2,1] 
a.sort()
print(f"{a}")

b = ['c','b','a'] 
b.sort()
print(f"{b}")

# 3 - reverse
a = ['c','b','a', 'd']
a.reverse()
print(f"{a}")

# 4 - Return Index
a = [1,2,3,4,5] 
a.index(5)
print(f"{a.index(1)}")
print(f"{a.index(5)}")

# 5 - insert
a = [1,2,3,4,5] 
a.insert(0,7) #(cord, contents)
print(f"{a}")

# 6 - remove
a = [1,2,3,4,5] 
a.remove(3) #not index, but contents itself
print(f"{a}")

# 7 - pop
a = [1,3,5,7] 
a.pop()
print(f"a : {a}")

# 8 - count contents
a = [1,2,3,4,5] 
print(f"{a.count(3)}")

a = [1,2,3,4,5] 
a.extend([4,5])
print(f"{a}")
b = [1,2,3,4,5]
a.extend(b)
print(f"{a}")