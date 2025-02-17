def count_zeroes(n):
    if n == 0:
        return 1
    elif n < 10:
        return 0
    else:
        if n % 10 == 0:
            return 1 + count_zeroes(n // 10)
        else:
            return 0 + count_zeroes(n // 10)

number = 10203040
result = count_zeroes(number)
print(f"The number of zeroes in {number} is {result}")