def linear_search(list, target):
    for i in list:
        if(list[i] == target):
            return i
    return -1


lis = [ 1, 2, 3, 0, -11, 245, 4, 5]
# linear_search(lis, 3)
print(linear_search(lis, 0))


