import sys

def eh_primo(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

dados = sys.stdin.read().split()
n = int(dados[0])
valores = dados[1:n+1]

resultados = []
for v in valores:
    x = int(v)
    if eh_primo(x):
        resultados.append(f"{x} eh primo")
    else:
        resultados.append(f"{x} nao eh primo")

print('\n'.join(resultados))