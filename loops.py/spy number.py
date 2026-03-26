# num=int(input("enter a number : "))
# sum=0
# product=1
# while num>0:
#     rem=num%10
#     sum=sum+rem
#     product=product*rem
#     num=num//10
# if sum==product:
#     print("spy number")
# else:
#     print("not a spy number ")

for i in range(1,1001):  
    temp=i
    sum=0
    product=1
    while temp>0:
        rem=temp%10
        sum=sum+rem
        product=product*rem
        temp=temp//10

    if sum==product:
        print(i,end=",")


