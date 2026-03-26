num=int(input("enter a number : "))
num1=num
num2=num
length = 0

while num>0:
    length=length+1   
    num=num//10
sum=0
while num1>0:
    rem=num1%10
    power=rem**length
    sum=sum+power
    num1=num1//10
if sum==num2:
    print("armstrong")
else:
    print("not a armstrong")