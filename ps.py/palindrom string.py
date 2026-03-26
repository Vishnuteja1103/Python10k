v=input("enter a string:")
rev=""
length=len(v)
i=0
while i<length:
    rev=v[i]+rev
    i=i+1
if v==rev:
    print("palindrom")
else:
    print("not a palindrom")





def pal(str):
    rev=""
    length=len(str)
    i=0
    while i <length:
        rev=str[i]+rev
        i=i+1
    if str==rev:
        print("palindrom")
    else:
        print("not a palindrom")

pal("mom")


