def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary(n // 2) + str(n % 2)

number = 13
result = decimal_to_binary(number)
print(f"The binary representation of {number} is {result}")