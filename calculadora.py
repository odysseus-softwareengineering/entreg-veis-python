"""Operações matemáticas reutilizáveis."""

def somar(a: float, b: float) -> float:
    """Devolve a soma de dois números."""
    return a + b


def subtrair(a: float, b: float) -> float:
    """Devolve a diferença entre dois números."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Devolve o produto de dois números."""
    return a * b


def dividir(a: float, b: float):
    """Devolve a divisão; retorna None quando o divisor é zero."""
    if b == 0:
        return None
    return a / b


if __name__ == "__main__":
    print(f"10 + 5 = {somar(10, 5)}")
    print(f"10 / 0 = {dividir(10, 0)}")
