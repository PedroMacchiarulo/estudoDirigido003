# ...existing code...
from __future__ import annotations
from typing import Any

# Exercício 6 — Sistema de Pagamentos

class Usuario:
    """Representa um usuário genérico com saldo."""
    def __init__(self, nome: str):
        self.nome = nome
        self.saldo = 0.0

    def adicionar_saldo(self, valor: float) -> None:
        self.saldo += float(valor)

    def __repr__(self) -> str:
        return f"Usuario(nome={self.nome!r}, saldo={self.saldo:.2f})"


class Pagamento:
    def __init__(self, usuario: Usuario, valor: float):
        self.usuario = usuario
        self.valor = float(valor)
        self.status = "pendente"

    def processar(self) -> bool:
        # Exemplo simplificado: processamento sempre bem-sucedido
        # Em mundo real, validaria gateway, transação etc.
        if self.valor <= 0:
            self.status = "falha"
            return False
        # Se o usuário tiver método adicionar_saldo, use-o; caso contrário, manipule atributo direto
        if hasattr(self.usuario, "adicionar_saldo"):
            self.usuario.adicionar_saldo(self.valor)
        else:
            if not hasattr(self.usuario, "saldo"):
                self.usuario.saldo = 0.0
            self.usuario.saldo += self.valor
        self.status = "concluido"
        return True

    def __repr__(self) -> str:
        return f"Pagamento(valor={self.valor}, status={self.status})"


if __name__ == "__main__":
    # Exemplo de uso
    u = Usuario("Ana")
    print("Antes:", u)

    p = Pagamento(u, 50.0)
    print("Pagamento criado:", p)

    sucesso = p.processar()
    print("Processado:", sucesso)
    print("Depois:", u)
    print("Pagamento:", p)
