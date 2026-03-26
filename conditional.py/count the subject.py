m=int(input("enter marks in maths :"))
p=int(input("enter marks in physics :"))
c=int(input("enter marks in chemistry  :"))
count=0
if m>=35:
    count=count+1
if p>=35:
    count=count+1
if c>=35:
    count=count+1
if count>=1:
    print("passed")
else:
    print("failed")

#---------------------------------------------------------------------------

m=int(input("enter marks in maths :"))
p=int(input("enter marks in physics :"))
c=int(input("enter marks in chemistry  :"))
count=0
if m>=35:
    count=count+1
if p>=35:
    count=count+1
if c>=35:
    count=count+1
if count>=2:
    print("passed")
else:
    print("failed")