# Exercício 5 — Gestão de Usuários de Jogo
class Jogador:
    def __init__(self, nome: str, saldo: float = 0.0):
        self.nome = nome
        self.saldo = float(saldo)
        self.itens = {}  # item -> quantidade

    def adicionar_saldo(self, valor: float):
        if valor < 0:
            raise ValueError("Não é possível adicionar saldo negativo.")
        self.saldo += float(valor)

    def comprar_item(self, item: str, preco: float, quantidade: int = 1):
        custo = float(preco) * int(quantidade)
        if custo > self.saldo:
            raise ValueError("Saldo insuficiente para compra.")
        self.saldo -= custo
        self.itens[item] = self.itens.get(item, 0) + int(quantidade)

    def __repr__(self):
        return f"Jogador({self.nome!r}, saldo={self.saldo:.2f}, itens={self.itens})"