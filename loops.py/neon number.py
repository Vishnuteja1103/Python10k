num=int(input("enter a number : "))
num1=num
power=num**2
power2=power
sum=0
while power2>0:
    rem=power2%10
    sum=sum+rem
    power2=power2//10
if num1==sum:
    print("neon number ")
else:
    print("not a neon number")
