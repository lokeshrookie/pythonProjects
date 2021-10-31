def binary_search(l, target):
    start = 0
    end = len(l) - 1

    while start<=end:
        mid = int(start+(end - start)/2)

        if target == l[mid]:
            return mid

        elif target < l[mid]:
            end = mid - 1

        elif target > l[mid]:
            start = mid + 1

    return -1


lis = [-221, 0, 2, 3, 4, 5, 6]
print(binary_search(lis, -221))
print(binary_search(lis, 0))
print(binary_search(lis, 3))
