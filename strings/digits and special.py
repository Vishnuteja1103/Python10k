# count the digits and special characters in a string ?
string=input("enter a string:")
digitcount=0
specialcharcters=0
for i in string:
    if ord(i)>=48 and ord(i)<=57:
        digitcount+=1
    elif i in " !@#$%^&*()_-+,./'[]\{|}:;<>? ":
        specialcharcters+=1

print("digit count:",digitcount)
print("specualcharcater:",specialcharcters)