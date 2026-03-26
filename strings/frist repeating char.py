#find the first repeating charecter from a string?
s=input("enter a string:")
d={}
sr=""
for i in s:
    if i in d:
        d[i]+=1
        if d[i]>1:
            sr=sr+i
            break
    else:
        d[i]=1
print(sr)