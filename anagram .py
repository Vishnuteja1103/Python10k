s1="silent"
s2="listen"
d1={}
d2={}
if len(s1)==len(s2):
    for i in s1:
        if i in d1:
            d1[i]+=1
        else:
            d1[i]=1
    
    for j in s2:
        if j in d2:
            d2[j]+=1
        else:
            d2[j]=1
    if d1==d2:
        print("anagram")
    else:
        print("not a anagram")
else:
    print("not anagaram")


# falsy
# arr=[0,1,False,2,'',3]
# d=[]
# for i in arr:
#     if isinstance(i, int) and i != 0:
#         d.append(i)

# print(d)


# arr=[0,1,False,2,'',3,2.0]
# d=[]
# for i in arr:
#     if i :
#         d.append(i)

# print(d)

# arr=[0,1,False,2,'',3,2.0]
# d=[]
# for i in arr:
#     if isinstance(i, float) and i != 0:
#         d.append(i)

# print(d)

# find the unique elements 
arr=[1,2,2,3,4,4,5]
l=[]
d={}
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for j in d:
    if d[j]==1:
        l.append(j)
print(l)




