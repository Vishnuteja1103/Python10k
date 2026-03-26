# find the number was strong number or not 

num=int(input("enter a number : "))
num2=num
sum=0
while num>0:
    rem=num%10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    sum=sum+fact
    num=num//10
# print(num)
# print(sum)
if num2==sum:
    print("strong number ")
else:
    print("not a strong number")

#------------------------------
#-strongnumber between (1 to 1000)----------

for i in range(1,1001):
    sum=0
    num=i
    while num>0:
        rem=num%10
        fact=1
        for j in range(1,rem+1):
            fact=fact*j
        sum=sum+fact
        num=num//10
    if i==sum:
        print(i)
