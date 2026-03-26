# l=list(map(int,input("enter  list:").split()))
# for i in range(len(l)):
#     if l[i] % 2 ==0:
#         print(f"{i} is even number")
#     else:
#         print(f"{i} is odd number")

# a=list(map(int,input("enter a list : ").split()))
# b=[]
# for i in range(len(a)):
#     b.append(a[i])

# print(b)

a=list(map(int,input("enter a list:").split()))
b=[]
for i in range(len(a)):
    if a[i] % 2 == 0:
        b.append(f"{a[i]} even")
    else :
        b.append(f"{a[i]} odd")
print(b)