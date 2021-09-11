# quicksort

num_count = int(input())
arr = []
for i in range (0, num_count):
    arr.append(int(input()))

def quick_sort(arr, start, end):
    middle = int((start + end) / 2)

    if arr[start] > arr[middle]:
        temp = arr[start]
        arr[start] = arr[middle]
        arr[middle] = temp
    if arr[middle] > arr[end]:
        temp = arr[middle]
        arr[middle] = arr[end]
        arr[end] = temp
    if arr[start] > arr[middle]:
        temp = arr[start]
        arr[start] = arr[middle]
        arr[middle] = temp
    if (end - start) > 2:
        pivot = arr[middle]
        temp = arr[end - 1]
        arr[end - 1] = arr[middle]
        arr[middle] = temp
    
        i = start
        j = end - 1
        while 1:
            i += 1
            while arr[i] < pivot and i < end:
                i += 1
            j -= 1
            while arr[j] > pivot and j > start:
                j -= 1
            if i >= j:
                break

            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        
        temp = arr[i]
        arr[i] = arr[end - 1]
        arr[end - 1] = temp

        quick_sort(arr, start, i - 1)
        quick_sort(arr, i + 1, end)

quick_sort(arr, 0, num_count - 1)
print(arr)