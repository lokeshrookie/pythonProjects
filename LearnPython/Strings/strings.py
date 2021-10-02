str = 'Lokesh is an IPS officer'
# print(str)
for i in range(len(str)):
    if str[i] == str[i-1]:
        print(str[i])
    else:
        continue


