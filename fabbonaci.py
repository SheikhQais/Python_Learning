def fabb(f1, f2, n):
    if n == 0:
        return f1
    else:
        print(f1)
        return fabb(f2, f1 + f2, n - 1)

f1 = 0
f2 = 1
n = 5
fabb(f1, f2, n)