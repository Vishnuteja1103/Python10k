name=input("enter a string:")
rev=""
length=len(name)
i=0
while i<length:
    rev=name[i]+rev
    i=i+1
if rev==name:
    print("palindrome")
else:
    print("not a palindrome")


# -------------------------------------------------

arr=[8,9,2,7,8]
s=set(arr)
b=[]
target=9
for i in s:
    if i<target:
        b.append(i)
print(b)


#--------------------------------------------------------------


arr = [8, 9, 2, 7, 8]
target = 9

result = []

for a in range(len(arr)):
    for j in range(a + 1, len(arr)):
        if arr[a] + arr[j] == target:
            result = [arr[a], arr[j]]
 

print(result)


#------------------------------------------------
arr=[2,7,5,7,9,8,2,7,6,2,9]
s=set(arr)
b=[]
for i in range(len(s)):
    if arr[i]>=0:
        b.append(arr[i])
print(b)


#---------------------------------------only dup---
 

arr = [8,2,7,9,5,7,8,9,2]
bu=[]
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            bu.append(arr[i])
print(bu)