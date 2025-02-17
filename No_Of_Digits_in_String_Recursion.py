def count_digits_in_string(s):
    if s == '':
        return 0
    else:
        if s[0].isdigit():
            return 1 + count_digits_in_string(s[1:])
        else:
            return 0 + count_digits_in_string(s[1:])

text = "Hello123World456"
result = count_digits_in_string(text)
print(f"The number of digits in the string is {result}")