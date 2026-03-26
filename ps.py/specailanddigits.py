#count the digits and special characters in a string
str=input("enter a string:")
count=0
for i in str:
    if (ord(i)>=95 and ord(i)<=122):
        count=0
    elif (ord(i)>=65 and ord(i)<=9):
        count=0
    elif (ord(i)>=48 and ord(i)<=57):
        count=count+1
    elif (ord(i)!=32):
        count+=1
print(count)