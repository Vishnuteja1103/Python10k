#---------prime number or not ----------

num=int(input("enter a number : "))
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print(f"{num} is a prime number ")
else:
    print(f"{num} is not a prime number ") 

#-------------------------------------------------------------
# print all the prime number in 1 to 100
for i in range(1,101):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count==2:
        print(i)
