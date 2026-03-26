def outer():
    print("prime or not ")
    def inner(num):
        count=0
        for i in range(1,num+1):
            # if i%2==0:
            #     count=count+1
            rem=num%10
            count=count+1
            num=num//10
        if count!=2:
            print("prime number")
        else:
            print("not aprime number")
    inner(5)
outer()