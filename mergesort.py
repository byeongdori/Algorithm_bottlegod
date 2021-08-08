# 수 정렬하기 2 - Using Merge Sort
import copy

num_count = int(input())
arr = []
for i in range (0, num_count):
    arr.append(int(input()))

def merge_sort(arr, left, right):

    middle = int((left + right) / 2)

    if left == right:
        return

    merge_sort(arr, left, middle)
    merge_sort(arr, middle + 1, right)
    merge(arr, left, right)

def merge(arr, left, right):

    temparr = [0 for i in range(num_count)]
    middle = int((left+right) / 2)

    first_arr_left = left
    first_arr_right = middle
    second_arr_left = middle + 1
    second_arr_right = right

    i = left
    while first_arr_left <= first_arr_right and second_arr_left <= second_arr_right:
        if arr[first_arr_left] > arr[second_arr_left]:
            temparr[i] = arr[second_arr_left]
            i += 1
            second_arr_left += 1
        else:
            temparr[i] = arr[first_arr_left]
            i += 1
            first_arr_left += 1
        
    if first_arr_left > first_arr_right:
        for j in range(second_arr_left, second_arr_right + 1):
            temparr[i] = arr[j]
            i += 1
    else:
        for j in range(first_arr_left, first_arr_right + 1):
            temparr[i] = arr[j]
            i += 1
    
    for i in range(left, right + 1):
        arr[i] = temparr[i]

merge_sort(arr, 0, num_count - 1)
print(arr)