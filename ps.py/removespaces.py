# remove spaces in a string

str=input("enter a string:")
op=""
for i in str:
    if i != " ":
        op+=i
print(op)