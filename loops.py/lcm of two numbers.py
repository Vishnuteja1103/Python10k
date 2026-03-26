num1=int(input("enter a number :"))
num2=int(input("enter a number :"))
largest=max(num1,num2)
while True:
    if largest%num1==0 and largest%num2==0:
        lcm=largest
        print(lcm)
        break
    largest+=1