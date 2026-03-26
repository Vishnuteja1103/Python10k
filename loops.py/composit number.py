num=int(input("enter a number :"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
        num=num//10
if count!=2:
    print("it was  composit number ")
else:
    print("it was not composite number")
