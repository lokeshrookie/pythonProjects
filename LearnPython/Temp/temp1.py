a = [1, 2, 88, 5, 5, 7]
b = [888888888888888888, "l", 6.88]

a.sort()
a.reverse()
a.extend(b)
print(a)
print(a.index(2))
# print(b)
# for i in a:
#     if a[i] == b[i]:
#         print(i)