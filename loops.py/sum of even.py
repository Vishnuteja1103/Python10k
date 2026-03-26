# wapp to sum of even numbers from 1 to 1000?
#---------using for loop-----

sum=0
for i in range (1,1001):
    if i%2==0:
        sum=sum+i
print(sum)

#------ using while loop ---------

i=1
sum=0
while i<=1000:
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)
