string=input("enter a string:")
string1=input("enter a string:")
d={}
d1={}
if len(string)!=len(string1):
    print("not a anagaram")
    pass
else:
    for i in string:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for j in string1:
        if j in d1:
            d1[j]+=1
        else:
            d1[j]=1    

if d==d1:
    print("anagaram")
else:
    print("not a anagaram")
