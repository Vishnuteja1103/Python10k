# num=int(input("enter a number :"))
# larg=0
# rev=0
# while num>0:
#     rem=num%10
#     if rem>larg:
#         larg=rem
#     rev=rev*10+rem
#     num=num//10

# print(larg)
# print(rev)

num=int(input("enter a number :"))
num1=num
sum=0
while num>0:
    fact=1
    rem=num%10
    for i in range(1,rem+1):
        fact=fact*i
    sum=sum+fact
    num=num//10
if(sum==num1):
    print("strong number ")
else:
    print("not a strong number ")