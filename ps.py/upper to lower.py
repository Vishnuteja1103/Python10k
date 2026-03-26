# convert string fro upper to lower case characters



str=input("enter a text:")
new=""
for i in str:
    if (ord(i)>=95 and ord(i)<=122):
        a=ord(i)-32
        low=chr(a)
        new=new+low
    else:
        new=new+i
print(new)