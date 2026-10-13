# A = int(input("Digite o valor de A: "))
# b = int(input("Digite o valor de B: "))
# SOMA = A + b
# print(f"SOMA = {SOMA}")

# print ("Hello World")

# if True:
#     print("Objeto indentado")
#     print("Ainda dentro do if")
# print ("Fora do if")

# if True:
#     print("Erro!")
# IdenationError: faltou indentar

# x = 10 
# print (x) #10
# x = 20 
# print (x) #20 
# x = "agora sou texto"
# print(x) #agora sou texto

# a, b, c = 1, 2, 3
# print(a, b, c) #1 2 3
# x = y = z = 0 
# print (x, y, z) # 0 0 0

# a, b = 5, 10 
# a, b = b, a
# print(a, b) #10 5

# inteiro =  42
# decimal = 3.14
# grande = 1_000_000
# negativo = -19
# cientifica = 2.5e3 #2500.0

# nome = "Python"
# frase = 'Aprendendo'
# texto = """varias linhas"""

#Atividade TechX 2026.2 Dia 17/08/2026
# a = float(input())
# b = float(input())
# c = float(input())
# media = (a * 2 + b * 3 + c * 5) / 10 
# print (f"MEDIA {media:.1f} ")

# idade = int(input("Digite sua idade: "))
# if idade >= 18:
#     print("Você é maior de idade")
# elif idade >= 12:
#     print("Você é adolescente")
# else:
#     print("Você é criança")

# nota1 = float(input("Digite a nota 1: "))
# nota2 = float(input("Digite a nota 2: "))
# nota3 = float(input("Digite a nota 3: "))
# media = (nota1 + nota2 + nota3) / 3
# print(f"Média: {media:.1f}")
# if media >= 7:
#     print("Aprovado")
# elif media >= 5:
#     print("Recuperação")
# else:
#     print("Reprovado")

# opcao = int(input("Digite uma opção (1-Iniciar, 2-Configurações): "))
# match opcao:
#     case 1:
#         print("Iniciar")
#     case 2:
#         print("Configurações")
#     case _:
#         print("Opção inválida")

# def classificar_cliente(idade, renda):
#     match idade, renda:
#         case idade, renda if idade >= 18 and renda >= 10000:
#             return "Diamante"
#         case idade, renda if idade >= 18 and renda >= 5000:
#             return "Ouro"
#         case idade, renda if idade >= 18 and renda >= 2000:
#             return "Prata"
#         case idade, renda if idade >= 18:
#             return "Bronze"
#         case idade, renda if idade < 18:
#             return "Cliente menor de idade - não classificado"
#         case _:
#             return "Dados inválidos"
# idade = int(input("Digite sua idade: "))
# renda = float(input("Digite sua renda mensal: "))
# categoria = classificar_cliente(idade, renda)
# print(f"\nCliente classificado como: {categoria}")

cores = ["azul", "verde", "vermelho"]
for cor in cores:
    print(cor)