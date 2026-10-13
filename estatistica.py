"""Desafios bônus de estatística simples."""
from statistics import median, multimode

def media(valores: list[float]) -> float:
    """Calcula a média de uma lista não vazia."""
    if not valores:
        raise ValueError("A lista não pode estar vazia.")
    return sum(valores) / len(valores)


def mediana(valores: list[float]) -> float:
    """Calcula a mediana de uma lista não vazia."""
    if not valores:
        raise ValueError("A lista não pode estar vazia.")
    return median(valores)


def moda(valores: list[float]) -> list[float]:
    """Retorna todas as modas; pode haver mais de uma."""
    if not valores:
        raise ValueError("A lista não pode estar vazia.")
    return multimode(valores)


def fatorial(numero: int) -> int:
    """Calcula fatorial recursivamente para inteiros não negativos."""
    if numero < 0:
        raise ValueError("O fatorial não está definido para negativos.")
    if numero in (0, 1):
        return 1
    return numero * fatorial(numero - 1)


def relatorio(titulo: str, *linhas, **config) -> str:
    """Monta um relatório simples usando linhas variáveis e opções nomeadas."""
    separador = config.get("separador", "-")
    cabecalho = f"{titulo}\n{separador * len(titulo)}"
    return "\n".join([cabecalho, *(str(linha) for linha in linhas)])