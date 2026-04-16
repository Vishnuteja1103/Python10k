def prime(num):
    count=0
    for i in range(1,num+1):
        if i%2==0:
            count+=1
    if count==2:
        print("prime")
    else:
        print("not a prime")

prime(5)