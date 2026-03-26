def perfect_or_not(num):
    num1=num
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    if sum==num1:
        return True
    else:
        return False
    

print(perfect_or_not(28))
