def count_odd_digits(n):
    if n == 0:
        return 0
    else:
        if n % 2 != 0:
            return 1 + count_odd_digits(n // 10)
        else:
            return 0 + count_odd_digits(n // 10)

number = 1234567
result = count_odd_digits(number)
print(f"The number of odd digits in {number} is {result}")