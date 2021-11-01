arr = [-111, -93, -11,  0, 1, 2, 3, 4, 5, 6, 7]

target = -11


def binary(lis, element):
    start = 0
    end = len(lis) - 1
    while start <= end:
        mid = (start + end) // 2  # use // operator
        if element == lis[mid]:
            return mid
        elif element < lis[mid]:
            end = mid - 1
        else:
            start = start + 1
    return -1


print(binary(arr, target))
