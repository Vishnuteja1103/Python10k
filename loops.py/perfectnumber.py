#----print the factors of a number ?

num=int(input("enter a number : "))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum==num:
    print(f"{num} is a prefect number 😎 ")
else:
    print(f"{num} is not a prefect number 😢 ")
        
#------------between 1 to 100 ------
for i in range(1,101):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum=sum+j
    if sum==i:
        print(i)

