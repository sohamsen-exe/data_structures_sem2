def count_digits(n):
    if n == 0:
        return 0
    else:
        return 1 + count_digits(n // 10)

number = 12345
result = count_digits(number)
print(f"The number of digits in {number} is {result}")