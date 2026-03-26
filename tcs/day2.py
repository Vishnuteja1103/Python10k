# for i in range(5):
#     for k in range(5-i):
#         print(" ",end="")
#     for j in range(i):
#         print("* ",end="")
#     print()
# for i in range(5,-1,-1):
#     for k in range(5-i):
#         print(" ",end="")
#     for j in range(i):
#         print("* ",end="")
#     print()
# ````````````````````````````````````````````````````````
# for i in range(5):
#     for k in range(5-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     print()
# for i in range(5,-1,-1):
#     for k in range(5-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     print()
# ````````````````````````````````````````````````````

# for i in range(5):
#     for j in range(i):
#         print("*",end="")
#     print()
# for i in range(5,-1,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

for i in range(5):
    for j in range(i):
        print("*",end="")
    for j in range(5-i-1):
        print(" ",end=" ")
    for j in range(i):
        print("*",end="")
    print()
for i in range(5-2,-1,-1):
    for j in range(i):
        print("*",end="")
    for j in range(5-i-1):
        print(" ",end=" ")
    for j in range(i):
        print("*",end="")
    print()

#     for j in range(5-i):
#         print(" ",end="")
#     for j in range(5-i-1):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     print()
# for i in range(5-1,-1,-1):
#     for j in range(i):
#         print("*",end="")
#     for j in range(5-i-1):
#         print(" ",end="")
#     for j in range(5-i-1):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     print()

 