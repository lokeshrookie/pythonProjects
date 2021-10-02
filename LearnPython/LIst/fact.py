
a = [5, 10, 25, 25, 30, 35, 40 ]
temp = []
for i in a:
    if temp.__contains__(i):
        print(i)
    else:
        temp.append(i)