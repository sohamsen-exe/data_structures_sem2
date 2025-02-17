def searching():
    listt = []
    n = int(input("Enter number of Elements: "))
    for i in range(n):
        e = int(input("Enter Element: "))
        listt.append(e)
    print("List :", listt)
    ch = int(input("Enter Element to search: "))
    for j in listt:
        if ch == j:
            print("Location is", listt.index(j))
searching()