num=int(input("enter a number : "))
while num>9:
    sum=0
    while num>0:
        rem=num%10
        sum=sum+rem
        num=num//10
    num=sum
print(sum)
if sum==1:
    print("magic number ")
else:
    print("not a magic number  ") 


for i in range(1,101):
    temp=i
    while i>9:
        sum=0
        while i>0:
            rem=i%10
            sum=sum+rem
            i=i//10
        i=sum
    if sum==1:
        print(temp)