#count the spaces in string

str=input("enter a string with spaces:")
count=0
sp=" "
for i in str:
    if i in sp:
        count=count+1
print(count)