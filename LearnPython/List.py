"""
IMPORTANT POINTS:
1. IN JAVA, LAST INDEX WILL BE (array.length-1) .But in Python, last index will be len(array).
Because, python will print the elements upto before last element but it will not print the element at the last index given.
"""

l1 = [1, 2, 3, 4, 5, 6]
l2 = [11, 22, 33, 44, 55, 66]
print(l1)  # Printing a list
print(l2)
print(len(l1))  # Printing the length of the list
print(len(l2))
print(l1 + l2)  # Concatination of two lists
print(l1, l2)  # Printing two lists on the same line
l2 = l2 + [77]  # Appending an element to the end of the list
print(l2)
print(len(l1) > len(l2), len(l1) < len(l2))
print(len(l1) < len(l2))

cars = ["Bugatti", 'Audi', "GTA", 'Mercedes', 'Lamborghini', 'Ferrari']
print(cars) # printing the Sstring type list.
print(cars[0]) # printing an element at desired index.
start = 0
end = len(cars)
"""
IMPORTANT POINTS:
1. IN JAVA, LAST INDEX WILL BE (array.length-1) .
But in Python, last index will be len(array)."""
print((cars[0:6])) # printing a range of elements in a list.
print(cars[start:end]) # printing elements from start to end.Here, the end will be 6.
# but the elements before the end index will only be printed.
print(len(cars))
cars1 = cars[0:3] # creating a sublist from the list cars.
cars2 = cars
print(cars1)
print(cars2)
# cars2 is a new variable name which is reference variable of cas.
# Any changes in cars2 will be reflected in cars.
cars2[0] = 'lokesh'
print(cars2)
print(cars)
print(cars[0:6:2])
"""
Systax is list[starting index : end index : """