# Find the Largest Element in an Array

# arr=[3, 1, 4, 1, 5, 9] 
# large=float("-inf")
# for i in arr:
#     if i>large:
#         large=i

# print(i)

# Find the Second Largest Element
# arr= [3, 1, 4, 1, 5, 9]
# large=float("-inf")
# sl=float("-inf")
# for i in arr:
#     if i>large:
#         sl=large
#         large=i
#     elif large>i>sl:
#         sl=i
# print(sl)

# Sum of All Elements

# arr=[1, 2, 3, 4]
# sum=0
# for i in arr:
#     sum+=i

# print(sum)

# Remove Duplicates from an Array
# arr=[1, 2, 2, 3, 4, 4, 5]
# ar=[]
# for i in arr:
#     if i in ar:
#         pass
#     else:
#         ar.append(i)

# print(ar)

# Check if Array is Sorted
# arr = [1, 2, 3, 4, 5]
# a = len(arr)
# is_sorted = True
# for i in range(a - 1):
#     if arr[i] > arr[i + 1]:
#         is_sorted = False
#         break
# print(is_sorted)

# Reverse an Array
# arr=[1, 2, 3, 4, 5]
# left=0
# right=len(arr)-1
# while left < right:
#     arr[left],arr[right]=arr[right],arr[left]
#     left+=1
#     right-=1
# print(arr)

# Write a function to reverse the elements in an array.
# def rev(arr):
#     left=0
#     right=len(arr)-1
#     while left < right:
#         arr[left],arr[right]=arr[right],arr[left]
#         left+=1
#         right-=1
#     return arr

# print(rev([1,2,3,4,5]))

# Remove Falsy Values
# arr = [0, 1, "false", 2, '', 3]
# a = []
# for i in arr:
#     if isinstance(i, int) and i != 0:
#         a.append(i)
# print(a) 

# Find Unique Elements
# arr=[1, 2, 2, 3, 4, 4, 5] #→ [1, 3, 5]
# ar={}
# a=[]
# for i in arr:
#     if i in ar:
#         ar[i] += 1
#     else:
#         ar[i] = 1
# for j in ar:
#     if ar[j] == 1:
#         a.append(j)
# print(a) 

# Sum of Even Numbers
# arr=[1, 2, 3, 4, 5] #→  6
# sum=0
# for i in arr:
#     if i%2==0:
#         sum+=i
# print(sum)

# Rotate an Array
# arr=[1, 2, 3, 4, 5] #→ [4, 5, 1, 2, 3]
# k=2 
# l1=arr[len(arr)-k:]
# l2=arr[:len(arr)-k]
# print(l1+l2)
# print(len(arr))

# Intersection of Two Arrays
# a1=[1, 2, 3]
# a2=[2, 3, 4] # → [2,3]
# a=[]
# if len(a1)<len(a2):
#     for i in a2:
#         if i in a1:
#             a.append(i)
#         else:
#             pass
# elif len(a1)>len(a2):
#     for i in a1:
#         if i in a2:
#             a.append(i)
#         else:
#             pass

# print(a)

# arr=[1, 2, 4, 5]#   → [3]
# a=[]
# for i in range(1,len(arr)):
#     if i not in arr:
#         a.append(i)
# print(a)

# Find the Maximum Product of Two Elements
# arr=[3, 5, -2, 8, 11] #→ 8*11 →88
# Write a function to find the maximum product of two elements in an array.
# arr=[3, 5, -2, 8, 11]
# large=0
# sl=0
# for i in arr:
#     if i >large:
#         large=i
# for i in arr:
#     if i >sl and i<large:
#         sl=i
# print(sl*large)

# Move Zeros to End
# Write a function that moves all zeros in an array to the end while maintaining the order of other elements.
# arr=[0, 1, 0, 3, 12]# → [1, 3, 12, 0, 0]
# l1=[]
# l2=[]
# for i in arr:
#     if i==0:
#         l2.append(i)
#     else:
#         l1.append(i)
# print(l1+l2)

# Pair Sum
# Write a function to find all pairs in an array whose sum is equal to a given target.
arr = [2, 4, 3, 5, 7, 8, 9]#[[2,5],[4,3]]
target = 7
l = []
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            l.append([arr[i], arr[j]])
print(l)





