#Finding GCD using MRCF method
def gcd_mrcf(m,n):
    for i in range(1, min(m,n) + 1):
        if (m % i) == 0 and (n % i) == 0:
            mrcf = i
    return (mrcf)
m = int(input("Enter first number :"))
n = int(input("Enter second number :"))
print("GCD of", m, "and", n, "is :", gcd_mrcf(m,n))