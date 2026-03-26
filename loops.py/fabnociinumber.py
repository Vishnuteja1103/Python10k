

#-------------------------------

num=int(input("enter a number : "))
a=0
b=1
for i in range(0,num+1):
    temp=a+b
    a=b
    b=temp
print(a)