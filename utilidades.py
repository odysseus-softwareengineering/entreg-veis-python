"""Funções auxiliares para exercícios de modularização."""

def converter_celsius_para_fahrenheit(celsius: float) -> float:
    """Converte uma temperatura em Celsius para Fahrenheit."""
    return (celsius * 9 / 5) + 32


def validar_senha(senha: str) -> bool:
    """Valida uma senha didática: ao menos 8 caracteres, uma letra e um dígito."""
    return (
        len(senha) >= 8
        and any(caractere.isalpha() for caractere in senha)
        and any(caractere.isdigit() for caractere in senha)
    )


def calcular_total_caixa(*precos: float) -> float:
    """Soma uma quantidade variável de preços."""
    return sum(precos)


def criar_ficha_aluno(**dados) -> dict:
    """Recebe dados nomeados e devolve uma cópia do dicionário de dados."""
    return dict(dados)


def adicionar_item_seguro(lista: list, item):
    """Cria uma cópia da lista e acrescenta o item sem alterar a lista original."""
    nova_lista = lista.copy()  # Cópia defensiva.
    nova_lista.append(item)
    return nova_lista


if __name__ == "__main__":
    print(f"25 °C = {converter_celsius_para_fahrenheit(25):.1f} °F")
    print(f"Senha válida? {validar_senha('python123')}")
    print(f"Total da caixa: R$ {calcular_total_caixa(10.0, 5.5, 2.0):.2f}")
    ficha = criar_ficha_aluno(nome="Raymundo", curso="Python", nota=9.0)
    print(f"Ficha do aluno: {ficha}")
    original = ["caderno", "caneta"]
    print(f"Lista nova: {adicionar_item_seguro(original, 'borracha')}")
    print(f"Lista original preservada: {original}")

# Versão em Portugal (pseudocódigo comentado):
# função converter_celsius_para_fahrenheit(celsius)
#   devolver (celsius * 9 / 5) + 32
# fimfunção
# função validar_senha(senha)
#   devolver comprimento(senha) >= 8 e contém_letra(senha) e contém_dígito(senha)
# fimfunção
# função calcular_total_caixa(precos variáveis)
#   total <- 0; para cada preco somar ao total; devolver total
# fimfunção
# função criar_ficha_aluno(dados nomeados)
#   devolver os dados recebidos
# fimfunção
# função adicionar_item_seguro(lista, item)
#   nova_lista <- cópia(lista); adicionar item; devolver nova_lista
# fimfunção
