"""Classifica um cliente por idade e renda mensal.

As faixas são regras demonstrativas, pois o enunciado não especifica os limites.
"""

def classificar_cliente(idade: int, renda: float) -> str:
    """Retorna a categoria do cliente de acordo com idade e renda."""
    if idade < 18 or renda < 0:
        return "Não elegível"
    elif renda < 2000:
        return "Bronze"
    elif renda < 5000:
        return "Prata"
    elif renda < 10000:
        return "Ouro"
    else:
        return "Diamante"


def main():
    # Converte as entradas de texto para os tipos numéricos necessários.
    idade = int(input("Idade do cliente: "))
    renda = float(input("Renda mensal (R$): "))
    categoria = classificar_cliente(idade, renda)
    print(f"Categoria do cliente: {categoria}")


if __name__ == "__main__":
    main()
