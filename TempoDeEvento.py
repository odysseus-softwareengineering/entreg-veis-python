import sys
import re
from datetime import datetime

dados = sys.stdin.read().split('\n')

# Remove linhas vazias no final, se houver
dados = [linha for linha in dados if linha.strip() != '']

dia_inicio = int(re.findall(r'\d+', dados[0])[0])
h1, m1, s1 = map(int, re.findall(r'\d+', dados[1]))

dia_fim = int(re.findall(r'\d+', dados[2])[0])
h2, m2, s2 = map(int, re.findall(r'\d+', dados[3]))

# Ano é irrelevante, mês é fixo em Abril (4)
inicio = datetime(2024, 4, dia_inicio, h1, m1, s1)
fim = datetime(2024, 4, dia_fim, h2, m2, s2)

diferenca = fim - inicio
total_segundos = int(diferenca.total_seconds())

dias = total_segundos // 86400
resto = total_segundos % 86400

horas = resto // 3600
resto %= 3600

minutos = resto // 60
segundos = resto % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")