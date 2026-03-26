text=input("enter a string:")
upper=0
lower=0
for i in text:
    if (ord(i)>=97 and ord(i)<=122):
        lower=lower+1
         
    elif  (ord(i)>=65 and ord(i)<=90):
        upper=upper+1

print("UPPER:",upper)
print("LOWEER:",lower)
