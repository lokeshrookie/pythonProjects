# n = int(input())

def product_of_nums(num):
    # condition for last digit or single digit
    if num % 10 == num:
        return num
    return (num % 10) * product_of_nums(num // 10)


print(product_of_nums(1243))
