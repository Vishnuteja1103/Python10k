# i=1
# while i<=5:
#     print("vishnu",i)
#     i=i+1


# i=5
# while i>=1:
#     print("vishnu", i ,end="")
#     i=i-1

name=input(("enter your name:"))

while name =="":
    print("you didn't enter your name ")
    name=input(("enter your name:"))
else:
    print(f"hello {name}")
