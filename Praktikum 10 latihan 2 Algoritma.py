def bubble_sort(arr, n=None):
    if n is None:
        n = len(arr)
    
    if n == 1:
        return arr
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i] 
    
    return bubble_sort(arr, n - 1)

arr = [11, 9, 25, 12, 33, 69, 100]
print("List sebelum disorting:", arr)

arr_sorted = bubble_sort(arr)
print("List setelah disorting:", arr_sorted)
