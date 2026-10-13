import sys

dados = sys.stdin.read().split()

pares = 0
impares = 0
positivos = 0
negativos = 0

for valor in dados:
    n = int(valor)
    
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1

print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")