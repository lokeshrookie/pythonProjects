new_list = [1, 2, 3]
print(new_list[2])



# Two ways to check an item in list

if 1 in new_list:print(True)  # Linear search  operation

for i in new_list:    # Manual Operation
    if i == 1:
        print(True)


new_list.append(4)
new_list.append(5)
new_list.remove(5)
print(new_list)
new_list.extend([7, 8, 9])
print(new_list)

