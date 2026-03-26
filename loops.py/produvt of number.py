num=int(input("enter a number : "))
product=1
while num>0:
    rem=num%10
    product=product*rem
    num=num//10
print(product)