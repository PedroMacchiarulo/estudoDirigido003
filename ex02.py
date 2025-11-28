# Exercício 2 — Refatorando com POO
# ============================

class Produto:
    def __init__(self, nome: str, quantidade: int, preco: float):
        self.nome = nome
        self.quantidade = int(quantidade)
        self.preco = float(preco)

    def adicionar(self, qtd: int):
        self.quantidade += int(qtd)

    def remover(self, qtd: int):
        qtd = int(qtd)
        if qtd > self.quantidade:
            raise ValueError("Quantidade insuficiente.")
        self.quantidade -= qtd

    def valor_total(self):
        return self.quantidade * self.preco

    def __repr__(self):
        return f"Produto(nome={self.nome!r}, qtd={self.quantidade}, preco={self.preco:.2f})"