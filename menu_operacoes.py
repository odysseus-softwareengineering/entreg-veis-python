"""Menu de quatro operações usando match/case (Python 3.10+)."""

def calcular(a: float, b: float, operacao: str):
    """Executa a operação escolhida; retorna None se a divisão for por zero."""
    match operacao:
        case "1":
            return a + b
        case "2":
            return a - b
        case "3":
            return a * b
        case "4":
            if b == 0:
                return None
            return a / b
        case _:
            raise ValueError("Opção inválida.")


def main():
    # Mostra as opções disponíveis antes de pedir os valores.
    print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
    opcao = input("Escolha uma operação: ").strip()
    try:
        primeiro = float(input("Primeiro número: "))
        segundo = float(input("Segundo número: "))
        resultado = calcular(primeiro, segundo, opcao)
        if resultado is None:
            print("Erro: não é possível dividir por zero.")
        else:
            print(f"Resultado: {resultado:.2f}")
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")


if __name__ == "__main__":
    main()