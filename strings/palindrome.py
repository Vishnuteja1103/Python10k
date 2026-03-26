string=input("enter a string:")
rev=""
for i in string:
    rev=i+rev
if string==rev:
    print("palindrome")
else:
    print("not a palindrome ")
