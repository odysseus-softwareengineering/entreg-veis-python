"""Lê um CSV, valida campos com regex e gera relatório de registros."""
import csv
import re
from datetime import datetime
from pathlib import Path


class FormatoInvalidoError(Exception):
    """Exceção personalizada para dados que não respeitam as regras esperadas."""


# Os padrões validam formatos comuns, não garantem por si só a validade real do dado.
EMAIL_RE = re.compile(r"^[\w.+-]+@[\w-]+(?:\.[\w-]+)+$")
CPF_RE = re.compile(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$")
TELEFONE_RE = re.compile(r"^(?:\(?\d{2}\)?\s?)?(?:9?\d{4})-?\d{4}$")
DATA_RE = re.compile(r"^\d{2}/\d{2}/\d{4}$")


def validar_email(email: str) -> bool:
    """Verifica o formato básico de e-mail."""
    return bool(EMAIL_RE.fullmatch(email.strip()))


def validar_cpf(cpf: str) -> bool:
    """Verifica apenas o formato do CPF; não calcula os dígitos verificadores."""
    return bool(CPF_RE.fullmatch(cpf.strip()))


def validar_telefone(telefone: str) -> bool:
    """Verifica um formato comum de telefone brasileiro."""
    return bool(TELEFONE_RE.fullmatch(telefone.strip()))


def validar_data(data: str) -> bool:
    """Valida formato e existência de uma data no padrão DD/MM/AAAA."""
    if not DATA_RE.fullmatch(data.strip()):
        return False
    try:
        datetime.strptime(data.strip(), "%d/%m/%Y")
        return True
    except ValueError:
        return False


def validar_registro(registro: dict) -> list[str]:
    """Devolve uma lista de campos inválidos; lança KeyError se faltar coluna."""
    campos_obrigatorios = ("email", "cpf", "telefone", "data", "idade")
    for campo in campos_obrigatorios:
        if campo not in registro:
            raise KeyError(f"Coluna obrigatória ausente: {campo}")

    invalidos = []
    if not validar_email(registro["email"]):
        invalidos.append("email")
    if not validar_cpf(registro["cpf"]):
        invalidos.append("cpf")
    if not validar_telefone(registro["telefone"]):
        invalidos.append("telefone")
    if not validar_data(registro["data"]):
        invalidos.append("data")

    try:
        idade = int(registro["idade"])
        if idade < 0 or idade > 120:
            raise FormatoInvalidoError("Idade deve estar entre 0 e 120.")
    except ValueError:
        invalidos.append("idade")
    except FormatoInvalidoError:
        invalidos.append("idade")

    return invalidos


def analisar_csv(caminho: str) -> None:
    """Analisa o CSV e imprime estatísticas de validade."""
    total = 0
    validos = []
    invalidos = []

    try:
        # with garante que o arquivo será fechado mesmo em caso de erro.
        with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            if leitor.fieldnames is None:
                raise KeyError("O CSV não possui cabeçalho.")
            for numero_linha, registro in enumerate(leitor, start=2):
                total += 1
                try:
                    campos_invalidos = validar_registro(registro)
                    if campos_invalidos:
                        invalidos.append((numero_linha, registro, campos_invalidos))
                    else:
                        validos.append((numero_linha, registro))
                except KeyError as erro:
                    print(f"Erro na linha {numero_linha}: {erro}")
                    invalidos.append((numero_linha, registro, ["colunas ausentes"]))
        # Se a leitura terminou sem exceções, informa sucesso.
        print("Leitura do arquivo concluída.")
    except FileNotFoundError:
        print(f"Erro: arquivo não encontrado: {caminho}")
        return
    except UnicodeDecodeError:
        print("Erro: o arquivo não está codificado em UTF-8.")
        return
    except KeyError as erro:
        print(f"Erro no cabeçalho do CSV: {erro}")
        return
    finally:
        # Executa independentemente de sucesso ou falha.
        print("Fim da tentativa de leitura.")

    print("\n=== RELATÓRIO DA ANÁLISE ===")
    print(f"Total de registros: {total}")
    print(f"Registros válidos: {len(validos)}")
    print(f"Registros inválidos: {len(invalidos)}")

    print("\nVálidos:")
    for linha, registro in validos:
        print(f"Linha {linha}: {registro.get('nome', '(sem nome)')}")

    print("\nInválidos:")
    for linha, registro, campos in invalidos:
        nome = registro.get("nome", "(sem nome)")
        print(f"Linha {linha}: {nome} — campos inválidos: {', '.join(campos)}")


if __name__ == "__main__":
    caminho_csv = Path(__file__).with_name("dados.csv")
    analisar_csv(str(caminho_csv))
