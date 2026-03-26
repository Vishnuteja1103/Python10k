#print the number 1 to 100 using both the loops.using for loop
for i in range(1,101):
    print(i)
#`````````````````````````````````````````
#print the number 1 to 100 using both the loops.using for while loop`
i=1
while i<=100:
    print(i)
    i=i+1

#print the numbers from 100 to 1 ? by using both the loops 

for i in range(100,0,-1):
    print(i)

#print the number from 100 to 1 ? by using while loop

i=100
while i>=1:
    print(f"😒 {i}")
    i=i-1


#
#sum of 1 to 100

sum=0
for i in range(0,101):
    sum=sum+i
print(sum)


i=1
sum=0
while i <=100:
    sum=sum+i
    i=i+1
print(sum)



#40 to 60 

sum=0
for i in range(40,61):
    sum=sum+i
print(sum)


i=40
sum=0
while i <=60:
    sum=sum+i
    i=i+1
print(sum)


# odd and even numbers betweeen 1 to 200 using for loop

for i in range(1,201):
    if i%2==0:
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")

# odd and even numbers betweeen 1 to 200 using for while

i=1
while i<=200:
    if i%2==0:
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number ")
    i=i+1
