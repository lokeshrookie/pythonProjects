# python program to remove the white spaces from a string

name = input().split() # split converts the input string to list
answer = ""
for i in range(len(name)):
    answer = answer + name[i]
print(answer)
