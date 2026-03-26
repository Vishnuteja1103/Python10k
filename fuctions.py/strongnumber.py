def strong_num(num):
    num1=num
    sum=0
    while num>0:
        rem=num%10
        fact=1
        for i in range(1,rem+1):
            fact=fact*i
        sum=sum+fact
        num=num//10
    if sum==num1:
        return "strong number"
    else:
        return "not a strong number"
    
print(strong_num(145)) 
