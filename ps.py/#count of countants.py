#count the consonants in a string
str=input("enter a string:")
vo=["a","e","i","o","u"]
count=0
for i in str:
    if i not in vo:
        count=count+1
print(count)
print(len(str))
