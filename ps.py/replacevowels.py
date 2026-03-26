# replace vowels with *
str=input("enter a string:")
op=""
for i in str:
    if i in "aeiouAEIOU":
        op+="*"
    else:
        op+=i
 
print(op)
        