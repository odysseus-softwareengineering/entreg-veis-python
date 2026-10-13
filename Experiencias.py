import sys

dados = sys.stdin.read().split()

n = int(dados[0])

idx = 1
coelhos = 0
ratos = 0
sapos = 0

for _ in range(n):
    quantia = int(dados[idx])
    tipo = dados[idx + 1]
    idx += 2
    
    if tipo == 'C':
        coelhos += quantia
    elif tipo == 'R':
        ratos += quantia
    elif tipo == 'S':
        sapos += quantia

total = coelhos + ratos + sapos

perc_coelhos = (coelhos / total) * 100
perc_ratos = (ratos / total) * 100
perc_sapos = (sapos / total) * 100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {perc_coelhos:.2f} %")
print(f"Percentual de ratos: {perc_ratos:.2f} %")
print(f"Percentual de sapos: {perc_sapos:.2f} %")