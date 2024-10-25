def find(x, a, n):
    found = False
    i = 0
    while (i<n) and not found:
        if a[i] == x:
            found = True
        i = i + 1
    return found
a = {2, 6, 3, 8}
find(9, a, len(a))