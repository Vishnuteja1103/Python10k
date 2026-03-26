num=int(input("enter a number : "))
large=0
while num>0:
    rem=num%10
    if rem>large:
        large=rem
    num=num//10
print(f"{large} 😢")
