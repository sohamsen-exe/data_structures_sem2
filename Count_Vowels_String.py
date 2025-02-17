def count_vowels(s):
    if s == '':
        return 0
    else:
        if s[0].lower() in 'aeiou':
            return 1 + count_vowels(s[1:])
        else:
            return 0 + count_vowels(s[1:])

text = "Hello, World!"
result = count_vowels(text)
print(f"The number of vowels in the string is {result}")