import sys

x, y = map(int, sys.stdin.read().split()[:2])
lo, hi = min(x, y), max(x, y)

soma = sum(n for n in range(lo + 1, hi) if n % 2 != 0)

print(soma)