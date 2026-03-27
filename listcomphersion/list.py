# # print even number 
l1=[1,2,3,4,5,6,7,8,9,0]
l=[i for i in l1 if i%2==0]
print(f"list{l}")

s1=(1,2,3,4,5,6,7,8,9,0)
s=tuple(i for i in s1 if i%2==0)
print(f"tuple{s}")

set={1,2,3,4,5,6,7,8,9,0}
se={ i for i in set if i %2==0}
print(f"set{se}") 


# # print odd numbes
l2=[1,2,3,4,5,6,7,8,9,0]
l=[i for i in l2 if i%2!=0]
print(l)

# print only character with contain a init
name=["korada","vishnu","teja"]
ls=[i for i in name for j in i if j in "a"]
print(ls)


# print only negative values in a list 
values=[-8,-2,1,2,4,-5]
v=[i for i in values if i <0]
print(v)

# create a comphersion with 1 to 19 nubers?
c0=[i for i in range(1,11)]
print(c0)


#convert all the string into upper case 
up=["vishnu","teja","korada"]
upper_case=[i.upper() for i in up ]
print(upper_case)

#extract vowels from a string
lis = ["vishnu", "teja", "korada"]
l = [j for i in lis for j in i if j in "aeiouAEIOU"]
print(l)

# replace negative numbers with zero
values=[-8,-2,1,2,4,-5]
v=[i if i>0 else 0 for i in values]
print(v)

# #find the length of each word?
l1=["vishnu","teja","korada"]
l=[len(i) for i in l1]
print(l)

#print numbers divisible by both 2 and 3?
num=[2,3,4,5,6,1,7,8,9]
ln=[i for i in num if i%2==0 and i%3==0]
print(ln)