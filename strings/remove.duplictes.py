# #remove all duplicate charecters in a string?
string=input("enter a string:")
emp=''
for i in string:
    if i in emp:
        pass
    else:
        emp=emp+i
print(emp)