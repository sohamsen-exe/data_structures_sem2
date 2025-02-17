def sum_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural_numbers(n - 1)

n = 5
result = sum_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is {result}")