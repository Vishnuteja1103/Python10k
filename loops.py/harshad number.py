num=int(input("enter a number : "))
temp=num
sum=0
while num!=0:
    rem=num%10
    sum=sum+rem 
    num=num//10
if temp%sum==0:
    print("harshad number ")
else:
    print("not a harshd number ")


for i in range(1,1001):
    temp=i
    sum=0
    while temp!=0:
        rem=temp%10
        sum=sum+rem
        temp=temp//10
    if i%sum==0:
        print(i)


