# # # sers :
# # # it is a collection of homogenous and tetroeneous data 
# # # set is mutable but data inside the set should be immutable 
# # # set are denoted by with {}
# # #  empty set=set()
# # #  it takes the dulpicate data but it automatically it the duplicates .
# s1={2,3}
# # # print(s1)
# # # print(type(s1))

# # # s1.add(5)
# # # s1.add("hello ")
# # # print(s1)

# # # s1.remove(5)
# # # # s1.remove(6)
# # # print(s1)

# s1.update([1234,123456,123456,2345678])
# s1.update("vishnu")
# s1.update("876543")
# print(s1)

# s1.discard(3,)
# s1.discard(5)
# print(s1)

# s1.pop()
# print(s1.pop())
# s1.pop()
# print(s1.pop())


# # s1={1,2,3,4,1,2,3,4,7,89,2,5,7,6,"a","b","c","d","e"}
# # s1.pop()
# # print(s1)


# union 
# s1={1,2,3}
# s2={3,4,5}
# s3=s1.union(s2)
# print(s3)

# s1={1,2,3}
# s2={3,4,5}
# s3={6,7}
# s4={8,9,0}
# s5=s1.union(s2,s3,s4)
# print(s5)
# s6=s1|s2|s3|s4
# print(s6)


#difference

# s1={1,2,3,4}
# s2={3,4,5,6}
# s3=s2.difference(s1)
# print(s3)

# s4=s2-s1
# print(s4)

# s1={1,2,3,4}
# s2={3,4,5,6}
# s3={5,7,8}
# s4=s2.difference(s1,s3)
# print(s4)

# intersection()
# it is used to print the common elements from both the sets

# s1={1,2,3,4,5}
# s2={1,2,3,3,3,3,7,8}
# s4={1,2,6,7,8}
# s3=s1.intersection(s2)
# print(s3)

# s4=s1&s2
# print(s4)

#symmetric_difference()
#it is used to print the non-common elements from the both the sets.(^)
#syntax: varname.symmteric_difference(iterables)
#we cannot perform the symetric difference on the multiple sets

# s1={1,2,3,4}
# s2={2,3,5,6}
# s4={2,3,4,5,8}
# # s3=s1.symmetric_difference(s2,s4) #TypeError: set.symmetric_difference() takes exactly one argument (2 given)

 
# s3=s1^s2^s4
# print(s3)

#issuperset

# s1={1,2,3,4}  #biggest
# s2={2,4} #small
# print(s1.issuperset(s2))

# #issubset()
# #it is used to check the child set is a subset of parent set or not.
# #return's boolean value.

# s1={1,2,3}
# s2={1,2,3,4,5}
# print(s1.issubset(s2))

#isdisjoint()
#it returns true when there are no common elements in both the sets.
#else returns false.

# s1={1,2,3,4,5}
# s2={7,8}
# print(s1.isdisjoint(s2))

# difference_update()
# it is used to print the non-common elements from a parenet set and 
# and modifies the parent set.
# syntax: varname.difference_update(iterables)

# s1={1,2,3,4}
# s2={2,3}
# s1.difference_update(s2)
# print(s1)

# # symmetric_difference_update()
# # it is used to print the non-common elements from a both sets and modifies the
# # original sets.

# s1={1,2,3,4}
# s2={3,4,5,6,7}
# s1.symmetric_difference_update(s2)
# print(s1)
