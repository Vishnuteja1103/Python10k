num=int(input("enter a number : "))
if num%2==0 and num%3==0 and num%6==0 :
    print(f"{num} is divisible by 2,3,6")
else:
    print(f"{num} is not divisible by 2,3,6")