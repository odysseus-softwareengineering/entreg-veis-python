"""Testes automatizados básicos usando unittest."""
import unittest
from sistema import ContaCorrente, ContaPoupanca, Cliente


class TestSistemaBancario(unittest.TestCase):
    """Verifica regras essenciais das classes do sistema."""

    def test_deposito(self):
        conta = ContaCorrente("Ana", 100)
        conta.depositar(50)
        self.assertEqual(conta.saldo, 150)

    def test_saque_sem_saldo(self):
        conta = ContaCorrente("Bruno", 10)
        with self.assertRaises(ValueError):
            conta.sacar(20)

    def test_rendimento_poupanca(self):
        conta = ContaPoupanca("Carla", 1000, 0.01)
        self.assertEqual(conta.calcular_rendimento(), 10)

    def test_email_invalido(self):
        conta = ContaCorrente("Diego", 0)
        with self.assertRaises(ValueError):
            Cliente("Diego", "email-invalido", conta)


if __name__ == "__main__":
    unittest.main()
