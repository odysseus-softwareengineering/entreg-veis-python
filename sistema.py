"""Exemplo de POO: contas bancárias, herança, encapsulamento e polimorfismo."""
from abc import ABC, abstractmethod


class Conta(ABC):
    """Classe abstrata que define o contrato básico de uma conta bancária."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        """Inicializa uma conta com titular e saldo não negativo."""
        self.titular = titular
        self.saldo = saldo_inicial  # Passa pelo setter para validar o valor.

    @property
    def titular(self) -> str:
        """Nome do titular da conta."""
        return self._titular

    @titular.setter
    def titular(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O titular deve ser um texto não vazio.")
        self._titular = valor.strip()

    @property
    def saldo(self) -> float:
        """Saldo atual da conta."""
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        self._saldo = float(valor)

    def depositar(self, valor: float) -> None:
        """Adiciona um valor positivo ao saldo."""
        if valor <= 0:
            raise ValueError("O depósito deve ser maior que zero.")
        self._saldo += valor

    def sacar(self, valor: float) -> None:
        """Saca um valor se for positivo e houver saldo suficiente."""
        if valor <= 0:
            raise ValueError("O saque deve ser maior que zero.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= valor

    @abstractmethod
    def calcular_rendimento(self) -> float:
        """Calcula o rendimento da conta; implementado nas classes concretas."""
        raise NotImplementedError

    def __str__(self) -> str:
        """Representação amigável da conta."""
        return f"{self.__class__.__name__} de {self.titular} — saldo R$ {self.saldo:.2f}"

    def __repr__(self) -> str:
        """Representação técnica resumida."""
        return f"{self.__class__.__name__}(titular={self.titular!r}, saldo={self.saldo!r})"


class ContaCorrente(Conta):
    """Conta corrente sem rendimento e com taxa mensal opcional."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0, taxa_mensal: float = 0.0):
        super().__init__(titular, saldo_inicial)
        self.taxa_mensal = taxa_mensal

    def calcular_rendimento(self) -> float:
        """Conta corrente não gera rendimento neste exemplo."""
        return 0.0

    def aplicar_taxa(self) -> None:
        """Deduz a taxa se houver saldo suficiente."""
        if self.taxa_mensal < 0:
            raise ValueError("A taxa não pode ser negativa.")
        if self.saldo < self.taxa_mensal:
            raise ValueError("Saldo insuficiente para cobrar a taxa.")
        self._saldo -= self.taxa_mensal


class ContaPoupanca(Conta):
    """Conta poupança que calcula rendimento percentual."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0, taxa_rendimento: float = 0.005):
        super().__init__(titular, saldo_inicial)
        if taxa_rendimento < 0:
            raise ValueError("A taxa de rendimento não pode ser negativa.")
        self.taxa_rendimento = taxa_rendimento

    def calcular_rendimento(self) -> float:
        """Devolve o rendimento estimado para um período."""
        return self.saldo * self.taxa_rendimento


class Cliente:
    """Representa uma pessoa que possui uma conta (composição)."""

    def __init__(self, nome: str, email: str, conta: Conta):
        """Cria um cliente e valida o e-mail de forma básica."""
        self.nome = nome
        self.email = email
        self.conta = conta

    @property
    def nome(self) -> str:
        """Nome do cliente."""
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        if not valor.strip():
            raise ValueError("O nome não pode ficar vazio.")
        self._nome = valor.strip()

    @property
    def email(self) -> str:
        """E-mail do cliente."""
        return self._email

    @email.setter
    def email(self, valor: str):
        if "@" not in valor or "." not in valor.split("@")[-1]:
            raise ValueError("Formato de e-mail inválido.")
        self._email = valor.strip()

    def __str__(self) -> str:
        """Representação amigável do cliente."""
        return f"Cliente: {self.nome} | E-mail: {self.email} | {self.conta}"

    def __repr__(self) -> str:
        """Representação técnica do cliente."""
        return f"Cliente(nome={self.nome!r}, email={self.email!r})"


class Banco:
    """Mantém uma coleção de contas e apresenta resultados polimórficos."""

    def __init__(self, nome: str):
        """Cria um banco com uma lista de contas vazia."""
        self.nome = nome
        self.contas: list[Conta] = []

    def adicionar_conta(self, conta: Conta) -> None:
        """Adiciona uma conta à coleção do banco."""
        self.contas.append(conta)

    def listar_rendimentos(self) -> None:
        """Chama o mesmo método em tipos diferentes de conta."""
        for conta in self.contas:
            # Polimorfismo: cada classe concreta implementa o rendimento à sua maneira.
            print(f"{conta} | Rendimento estimado: R$ {conta.calcular_rendimento():.2f}")

    def __str__(self) -> str:
        """Representação do banco."""
        return f"Banco {self.nome} — {len(self.contas)} conta(s)"


def criar_contas_de_exemplo() -> list[Conta]:
    """Cria dez instâncias de contas de diferentes classes."""
    contas: list[Conta] = []
    for indice in range(1, 6):
        contas.append(ContaCorrente(f"Cliente Corrente {indice}", indice * 100.0, taxa_mensal=5.0))
    for indice in range(1, 6):
        contas.append(ContaPoupanca(f"Cliente Poupança {indice}", indice * 200.0, taxa_rendimento=0.01))
    return contas


def main():
    """Demonstra as classes, polimorfismo e tratamento de entradas inválidas."""
    banco = Banco("Banco Exemplo")
    contas = criar_contas_de_exemplo()

    for conta in contas:
        banco.adicionar_conta(conta)

    print(banco)
    banco.listar_rendimentos()

    # Demonstração de composição: um Cliente tem uma Conta.
    cliente = Cliente("Raymundo", "raymundo@example.com", contas[0])
    print(f"\n{cliente}")

    # Testa validações de forma controlada.
    try:
        ContaCorrente("Conta Inválida", -50)
    except ValueError as erro:
        print(f"\nErro tratado corretamente: {erro}")

    try:
        cliente.email = "email-sem-formato"
    except ValueError as erro:
        print(f"Erro tratado corretamente: {erro}")


if __name__ == "__main__":
    main()
