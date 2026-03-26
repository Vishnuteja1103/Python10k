# numbers = [10, 3, 7, 4, 11, 15, 23, 8]

# prime_numbers = []

# for num in numbers:
#     if num > 0:
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 break
#         else:
#             prime_numbers.append(num)

# print( prime_numbers)



l1=[1,2,3,4,5,6]
l=[]
for i in l1:
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1

    if count==2:
        l.append(i)

print(l)