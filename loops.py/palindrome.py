num=int(input("enter a number : "))
num2=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if rev==num2:
    print("palindrom")
else:
    print("not a palindrom")
