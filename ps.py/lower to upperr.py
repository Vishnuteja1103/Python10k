# convert string fro lower to upper case characters



str=input("enter a text:")
new=""
for i in str:
    if (ord(i)>=65 and ord(i)<=90):
        a=ord(i)+32
        low=chr(a)
        new=new+low
    else:
        new=new+i
print(new)