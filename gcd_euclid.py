def euclid_gcd(m,n):
    if m < n:
        m, n = n, m
    if n == 0 :
        return m
    else:
        return euclid_gcd(n, m % n)
m = int(input("Enter a Number :"))
n = int(input("Enter another Number :"))
print(euclid_gcd(m,n))