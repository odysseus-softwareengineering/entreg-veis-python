"""Cadastro, filtragem, ordenação e estatísticas de produtos."""

def main():
    produtos = []

    # Pergunta quantos produtos serão cadastrados e valida que seja positivo.
    while True:
        try:
            quantidade = int(input("Quantos produtos deseja cadastrar? "))
            if quantidade <= 0:
                print("Informe pelo menos um produto.")
                continue
            break
        except ValueError:
            print("Digite um número inteiro válido.")

    for indice in range(quantidade):
        print(f"\nProduto {indice + 1}")
        nome = input("Nome: ").strip()
        while not nome:
            nome = input("O nome não pode ficar vazio. Digite novamente: ").strip()

        while True:
            try:
                preco = float(input("Preço (R$): "))
                if preco < 0:
                    print("O preço não pode ser negativo.")
                    continue
                break
            except ValueError:
                print("Digite um preço numérico válido.")

        categoria = input("Categoria: ").strip().title()
        produtos.append({"nome": nome, "preco": preco, "categoria": categoria})

    # Filtra por preço acima do limite informado.
    limite = float(input("\nMostrar produtos acima de qual preço? R$ "))
    filtrados = [produto for produto in produtos if produto["preco"] > limite]

    # sort() altera a lista em si; sorted() cria uma nova lista.
    crescente = produtos.copy()
    crescente.sort(key=lambda produto: produto["preco"])
    decrescente = sorted(produtos, key=lambda produto: produto["preco"], reverse=True)

    categorias_unicas = {produto["categoria"] for produto in produtos}
    precos = [produto["preco"] for produto in produtos]
    estatisticas = (min(precos), max(precos), sum(precos) / len(precos))

    print("\n=== RELATÓRIO DE PRODUTOS ===")
    print("\nTodos os produtos:")
    for produto in produtos:
        print(f"- {produto['nome']} | R$ {produto['preco']:.2f} | {produto['categoria']}")

    print(f"\nProdutos acima de R$ {limite:.2f}:")
    if filtrados:
        for produto in filtrados:
            print(f"- {produto['nome']} | R$ {produto['preco']:.2f}")
    else:
        print("Nenhum produto corresponde ao filtro.")

    print("\nOrdem crescente:")
    for produto in crescente:
        print(f"- {produto['nome']}: R$ {produto['preco']:.2f}")

    print("\nOrdem decrescente:")
    for produto in decrescente:
        print(f"- {produto['nome']}: R$ {produto['preco']:.2f}")

    print(f"\nCategorias únicas: {', '.join(sorted(categorias_unicas))}")
    print(
        f"Estatísticas (menor, maior, média): "
        f"(R$ {estatisticas[0]:.2f}, R$ {estatisticas[1]:.2f}, R$ {estatisticas[2]:.2f})"
    )


if __name__ == "__main__":
    main()

# Versão em Portugal (pseudocódigo comentado):
# ler quantidade de produtos
# para cada produto: ler nome, preço e categoria; guardar no vetor
# para cada produto, se preço > limite, mostrar produto
# ordenar cópia do vetor por preço crescente com bubble sort:
#   comparar posições vizinhas; trocar quando o preço da esquerda for maior
# ordenar decrescente invertendo o critério da comparação
# simular conjunto de categorias: adicionar categoria apenas se ainda não existir
# calcular menor, maior e média percorrendo os preços
# apresentar o relatório final
