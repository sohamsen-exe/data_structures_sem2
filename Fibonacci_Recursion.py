def fib_a(n):
    if n == 0:
        return 0
    else:
        return fib_b(n - 1)

def fib_b(n):
    if n == 1:
        return 1
    else:
        return fib_a(n - 1) + fib_b(n - 1)

n = 10
for i in range(n):
    print(fib_a(i), end = " ")