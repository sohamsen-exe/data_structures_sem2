def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

result = gcd(48, 18)
print(f"The GCD is {result}")