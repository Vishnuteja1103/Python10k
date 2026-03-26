l1=[1,2,3,4,0]
largest=float("-inf")
second_largest=float("-inf")
for i in l1:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i!=largest:
        second_largest=i

print(second_largest)
    
 
