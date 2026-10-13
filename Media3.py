import sys

dados = sys.stdin.read().split()

n1 = float(dados[0])
n2 = float(dados[1])
n3 = float(dados[2])
n4 = float(dados[3])

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(dados[4])
    print(f"Nota do exame: {exame:.1f}")
    
    media_final = (media + exame) / 2
    
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print(f"Media final: {media_final:.1f}")