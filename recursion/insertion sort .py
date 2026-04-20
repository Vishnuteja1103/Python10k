def insertion_sort(arr):
    for i in range(1, len(arr)):## Traverse from the second element
        key = arr[i]      # Element to be inserted
        j = i - 1
        while j >= 0 and arr[j] > key: ## Move elements greater than key one position ahead
            arr[j + 1] = arr[j]
            j -= 1     
        arr[j + 1] = key ## Place the key in its correct position
    return arr
numbers = [64, 25, 12, 22, 11]
sorted_numbers = insertion_sort(numbers)

print("Sorted array:", sorted_numbers)