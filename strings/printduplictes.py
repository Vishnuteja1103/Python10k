# print only duplicate charecters from a string?
string=input("enter a string:")
d={}
s=''
for i in string:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
for i in d:
    if d[i]>1:
        s=s+i
print(s)
