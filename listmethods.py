#remove()
# l1=[1,2,3,4,5]
# print(l1.pop())

# print(l1.pop(2))
# print(l1.pop(-1))



l1=["hi","friends","maku",["pandagaledu","friends"]]
l2=l1.copy()
l1.append(1)
l2.append(4)
print(l1)
print(l2)
print(id(l1))
print(id(l2))
l1.append(4)
l1[3].append("prends")
print(l1)
print(l2)
print(id(l1[3]))
print(id(l2[3]))