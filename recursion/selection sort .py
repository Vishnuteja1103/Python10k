def selection_sort(arr):
    n=len(arr)
    for i in range(n): #12
        min_index=i #12
        for j in range(i+1,n): #34 to last 
            if arr[j]<arr[min_index]: #
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i] #swaping was done 

    return arr

num=[12,34,57,9,21,20] 
ss=selection_sort(num)   
print(ss)