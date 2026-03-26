# factorial of number
#---------- using for loop ---------

num=int(input("enter a number : "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)


#----- using while loop ----------

num=int(input("enter a number : "))
i=1
fact =1 
while i<=num:
    fact=fact*i
    i=i+1
print(fact)