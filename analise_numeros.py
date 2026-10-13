"""Lê cinco números e calcula soma, média, maior e menor."""

def main():
    numeros = []
    # range(5) repete exatamente cinco vezes.
    for indice in range(5):
        numero = float(input(f"Digite o {indice + 1}º número: "))
        numeros.append(numero)

    soma = sum(numeros)
    media = soma / len(numeros)
    maior = max(numeros)
    menor = min(numeros)

    print(f"Soma: {soma:.2f}")
    print(f"Média: {media:.2f}")
    print(f"Maior número: {maior:g}")
    print(f"Menor número: {menor:g}")


if __name__ == "__main__":
    main()
