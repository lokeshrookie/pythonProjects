n = int(input())


def print_numbers(num):
    print(num)
    if num == 1:
        return
    print_numbers(num - 1)


print_numbers(n)
