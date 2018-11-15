def f(a):
    print(a)
    del a[2:]
    print(a)

b = [1,2,3]
f(b)
print(b)
