# n=4
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()

#-------------------------------------------
# n=5
# for i in range(n):
#     for j in range(n):
#         if( i==0 or j==0 or j==n-1 or i==n-1 ):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#--------------------------------------
# n=6
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i):
#         if (j==i-1 or j==0 or i==n-1 ):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i):
#         if (j==i-1 or j==0 or i==n-1 ):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()

#-----------------------------
# n=6
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i):
#         if (j==i-1 or j==0  ):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i):
#         if (j==i-1 or j==0 ):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()

# prime number or not 
# num=int(input("enter a number:"))
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#     print(num,"is  prime number ")
# else:
#     print(num,"is not  prime number")

# ---------------------------------
count=0
for num in range(1,101):

    for i in range(1,num+1):
        if num%i==0:
            count+=1
if count==2:
    print(i)
