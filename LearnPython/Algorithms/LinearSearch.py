def linear_search(list, target):
    for i in range(0, len(lis)):
        if list[i] == target:
            return i
    return None


lis = [1, 2, 3, 0, -11, 245, 4, 5]

print(linear_search(lis, 0))

