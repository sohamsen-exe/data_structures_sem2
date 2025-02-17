def simple_gcd(m,n):
    fm = []
    for i in range(1, m + 1):
        if (m % i) == 0:
            fm.append(i)
    print("\nFactors of First Number :", fm)

    fn = []
    for j in range(1,n+1):
        if (n % j) == 0:
            fn.append(j)
    print("Factors of Second Number :", fn)

    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)
    print("Common Factors :", cf)

    return(cf[-1])
m = int(input("Enter a number :"))
n = int(input("Enter another number :"))
print("\nGreatest Common Divisor :", simple_gcd(m, n))