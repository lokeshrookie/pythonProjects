n = int(input())


def print_numbers(num):
    print(num)
    if num == n:
        return
    print_numbers(num +1)


print_numbers(1)

