def string_length(s):
    if s == '':
        return 0
    else:
        return 1 + string_length(s[1:])

text = "Hello, World!"
result = string_length(text)
print(f"The length of the string is {result}")