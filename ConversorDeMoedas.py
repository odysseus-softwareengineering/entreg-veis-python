valor_reais = float(input("Digite o valor em reais: "))
cotacao_dolar = float(input("Digite a cotação do dólar: "))
valor_dolar = valor_reais / cotacao_dolar
print(f"{valor_reais:.2f} reais equivalem a {valor_dolar:.2f} dólares.")