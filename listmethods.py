#remove()
# l1=[1,2,3,4,5]
# print(l1.pop())

# print(l1.pop(2))
# print(l1.pop(-1))


#copy
#shallowcopy
# l1=["hi","friends","maku",["pandagaledu","friends"]]
# l2=l1.copy()
# l1.append(1)
# l2.append(4)
# print(l1)
# print(l2)
# print(id(l1))
# print(id(l2))
# l1.append(4)
# l1[3].append("prends")
# print(l1)
# print(l2)
# print(id(l1[3]))
# print(id(l2[3]))

#deepcopy
# from copy import deepcopy
l1=[1,2,3,4,[5,6,7]]
# l2=deepcopy(l1)
# print("outer")
# print(l1)
# print(l2)
# print(id(l1))
# print(id(l2))
l1.append("sal ram")
# l2.append("friends")
# print("inner")
# print(l1)
# print(l2)
# print(id(l1[-1]))
# print(id(l2[-1]))

#packing and unpacking 
l1=[1,2,3,4,5]
a,b,*c=l1
print(l1)
print(a)
print(b)
print(c)