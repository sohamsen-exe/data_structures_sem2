def array_product(arr):
    n = len(arr)
    prod_arr = []
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= arr[j]
        prod_arr.append(product)
    return prod_arr

n = int(input("Enter number of Elements :"))
arr = [int(input("Enter Element :")) for i in range(n)]
print(array_product(arr))
