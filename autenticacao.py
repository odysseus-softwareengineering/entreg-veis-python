"""Autenticação simples com no máximo três tentativas."""

def autenticar(senha_correta: str) -> bool:
    """Pede a senha até acertar ou atingir três erros."""
    tentativas = 0
    while tentativas < 3:
        senha = input("Digite a senha: ")
        if senha == senha_correta:
            print("Acesso autorizado.")
            return True

        tentativas += 1  # Atualiza o contador para evitar loop infinito.
        restantes = 3 - tentativas
        if restantes:
            print(f"Senha incorreta. Tentativas restantes: {restantes}.")
    print("Acesso bloqueado após três erros.")
    return False


if __name__ == "__main__":
    autenticar("python123")
