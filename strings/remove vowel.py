string=input("enter a string:")
s=""
for i in string:
    if i not in "aeiouAEIOU":
        s=s+i
print(s)
