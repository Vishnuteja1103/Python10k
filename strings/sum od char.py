#sum of ascii values of each charecter in a string?
s=input("enter  a string:")
sum=0
for i in s:
    sum=sum+ord(i)
print(sum)