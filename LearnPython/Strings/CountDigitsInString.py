text = input()
count = 0
for i in text:
    if i.isdigit():
        count += 1
print(count)
print(text.count('a')) # this line counts the no of 'a' in text.


