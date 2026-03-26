# second largest number in a number
num=int(input("enter a number : "))
largest=0
smallest=0
while num>0:
    rem=num%10
    if rem>largest:
        smallest=largest
        largest=rem
    elif rem>smallest and rem!=largest:
        smallest=rem
    num=num//10
print(smallest)