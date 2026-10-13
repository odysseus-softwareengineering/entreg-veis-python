import sys

dados = sys.stdin.read().split()

for valor in dados:
    senha = int(valor)
    if senha == 2002:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")