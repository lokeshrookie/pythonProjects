
# 2-d Array
"""
We have to enter how many rows in line 1.
and then elemetns of each row.
then the two dimension array will be printed.
"""
lis = []
n = int(input())
for i in range(n):
    sub = list(map(int, input().split()))
    lis.append(sub)

print(lis)
