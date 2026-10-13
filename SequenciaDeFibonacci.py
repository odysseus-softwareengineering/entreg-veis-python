n = int(input())

fib = []
a, b = 0, 1
for _ in range(n):
    fib.append(a)
    a, b = b, a + b

print(' '.join(map(str, fib)))