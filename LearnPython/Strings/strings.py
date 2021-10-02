str = 'Lokesh is an IPS officer'
print(str)
if("IPS" in str):
        print("IPS")
for i in range(len(str)):
    if str[i] == str[i-1]:
        print(str[i])
    else:
        continue


