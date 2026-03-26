s=input("enter a string:")
count=0
z=0
vowels=["a","i","e","u","o"]
length=len(s)
while z<length:
    if s[z] in vowels:
        count=count+1
    z=z+1
print(count)


 