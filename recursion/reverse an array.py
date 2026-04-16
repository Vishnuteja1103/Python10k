# arr=[1,2,3,4,5,6]

# left =0
# right=len(arr)-1

# while left <  right :
#     arr[left],arr[right]=arr[right],arr[left]
#     left +=1
#     right -=1

# print(arr)


#  using def 
# def rev(arr):
#     left=0
#     right=len(arr)-1

#     while left<right:
#         arr[left],arr[right]=arr[right],arr[left]
#         left+=1
#         right-=1
#     return arr

# print(rev([1,2,3,4,5]))

# using recursion

def rev(arr2,left,right):
    if left>=right:
        return arr2
    arr2[left],arr2[right]=arr2[right],arr2[left]
    return rev(arr2,left+1,right-1)

arr=[1,2,3,4,5]
print(rev(arr,0,len(arr)-1))
# print(arr)