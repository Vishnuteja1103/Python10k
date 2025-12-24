# l1=[1,2,3,4,[2,3,4],5,6]
# print(l1[4][1])

# l1=["vishnu",11,"srinu",465789,12345,[2345],"jyothi",19]
# # print(l1[3])
# e1=l1[3]
# e2=e1[0]
# print(e2)
# # print(l1[4])

# l1=[1,2,3,4]
# print(l1)
# l2=[1,1,1,2,3,4,5]
# print(l2)

# l1=[1,2,2.3,True,False,"hello",2+3j]
# print(l1)


#list indexing
#postivte indexing 

# fruits=["apple","banana","orange","kiwi","avacodo"]
# e1=fruits[1]
# print(e1)
# print(fruits)
# e2=fruits[3]
# print(e2)
# e3=fruits[2]
# print(e3)

# l1=[1,2,3,4,[5,6]]
# print(l1[4])
# print(l1[4][0])
# print(l1[4][1])

# l1=[1,2,3,4,[5,6,[1,[3]]],[30]]
# print(l1[4][2][0])
# print(l1[5][0])
# print(l1[4][2][0])

#negative indexing:

# l1=[1,2,3,4,5,6]
# print(l1[-2])
# print(l1[-4])
# print(l1[-1])

# l1=[1,2,3,["a","b",["hello"]]]
# print(l1[-1][-1]) #hello
# print(l1[-1][-1]) #b
# print(l1[-1][-1][0][-4])

#list updating the values

# l1=[1,2,3,4,5]
# l1[0]="hello"
# l1[0]="hi" 
# l1[2]="three"
# print(l1)

# l1=[1,2,3,4,5]
# l1[5]="five"
# print(l1)


# l1=["apple","banana","mango",[1,2]]
# e1=l1[-1]
# print(e1)
# e1[1]="hello everyone"
# print(e1)
# l1[1]="one"
# print(l1)
# print(e1)

#list slicing 

l1=[1,3,5,7,"vishnu","teja","korada",["hello"]]
print(l1[:4])
print(l1[::-1])
print(l1[::1])