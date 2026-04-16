# def adttion(num1,num2):
#     print(num1+num2)

# adttion(20,11)


# def addition(a,b):
#     return a+b

# sum=addition(10,11)
# print(sum)

# 

# def num(a):
#     if a==0:
#         return
#     else:
#         num(a-1)
#         print(a)
# num(10)


# def name(a):
#     if a==0:
#         return
#     else:
#         name(a-1)
#         print("vishnu")

# name(10)

#  print the name n th times
# def name1(n,name):
#     if n<=0:
#         return
#     print(name)
#     name1(n-1,name)

# name1(5,"teja")


# print the numbers to n th to nth 
# def num(i,n):
#     if i>n:
#         return
#     print(i)
#     num(i+1,n)

# num(1,10)

#  print the numbers from n to 1 in reverse 
def num(i,n):
    if n<i:
        return
    print(n)
    num(i,n-1)

num(1,5)