n = int(input())


def sum_of_digits(num):
    if num == 0:
        return 0
    return num%10 + sum_of_digits(num//10)


print(sum_of_digits(n))