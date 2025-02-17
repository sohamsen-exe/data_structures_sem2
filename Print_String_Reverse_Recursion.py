def print_reverse(s):
    if s == '':
        return
    else:
        print_reverse(s[1:])
        print(s[0], end='')

text = "Hello, World!"
print_reverse(text)