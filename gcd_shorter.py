def gcd(m,n):
    cf = []
    for i in range(1, min(m, n) + 1):
        if (m % i) == 0 and (n % i) == 0:
            cf.append(i)
    print("GCD of ", m, "and ", n, "is :", cf[-1])
m = int(input())
n = int(input())
gcd(m,n)