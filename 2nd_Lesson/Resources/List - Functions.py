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