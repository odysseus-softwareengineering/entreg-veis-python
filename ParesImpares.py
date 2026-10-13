N = int(input())

pares = []
impares = []

for _ in range(N):
    numero = int(input())

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

pares.sort()
impares.sort(reverse=True)

for numero in pares:
    print(numero)

for numero in impares:
    print(numero)