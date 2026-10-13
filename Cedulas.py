n = int(input())
print(n)
notas = [100, 50, 20, 10, 5, 2, 1]
valor = n
for nota in notas:
    qtd = valor // nota
    valor = valor % nota
    print(f"{qtd} nota(s) de R$ {nota},00")