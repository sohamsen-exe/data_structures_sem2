def gcd_while(m, n):
    i = min(m, n)

    while i > 0:
        if ((m % i) == 0) and ((n % i) == 0):
            return(i)
        else:
            i -= 1
m = int(input("Enter a number :"))
n = int(input("Enter another number :"))
print(gcd_while(m, n))