count=0
num=int(input("enter a number : "))
for i in range(1,num+1):
    if num%i==0:
        count=count+1
        print(f"{i}",end=",")
print(f"\ncount:{count}")