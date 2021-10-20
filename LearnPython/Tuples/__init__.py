# Tuples are immutable where lists are immutable
tup = (1,2,3,4,5)
tup.count(3)
print(tup.count(5))
print(tup.index(5))