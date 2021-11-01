array = [-11, 0, 1, 2, 3, 4, 5, 6, 7, 8]
key = -11


def binary_search(arr, target, start, end):
    if start > end:
        return -1
    mid = (start+end)//2  # use floor division operator
    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, start, mid-1)
    elif target > arr[mid]:
        return binary_search(arr, target, mid+1, end)
    return -1


print(binary_search(array, key, 0, len(array) - 1))
