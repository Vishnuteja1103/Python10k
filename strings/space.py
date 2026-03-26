string=input("enter a string:")
count=0
for i in string:
    if i in " ":
        count+=1
print("space count:",count)