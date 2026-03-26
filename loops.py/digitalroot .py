num=int(input("enter a number : "))
while num>9:
    sum=0
    while num>0:
        rem=num%10
        sum=sum+rem
        num=num//10
    num=sum
print(sum)
if sum<9:
    print("digital root")
else:
    print("not a digital root ")

# num=int(input("enter a number : "))
# if num>10:
#     while num>9:
#         sum=0
#         while num>0:
#             rem=num%10
#             sum=sum+rem
#             num=num//10
#         num=sum
#     print(sum)
#     if sum<9:
#         print("digital root")
#     else:
#         print("nota a digital root ")
# else:
#     print("number is already a single digit ")


 
 