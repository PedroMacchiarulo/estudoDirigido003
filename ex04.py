class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto: Produto, quantidade: int = 1):
        self.itens.append((produto, int(quantidade)))

    def listar_produtos(self):
        return [(p.nome, q, p.preco) for p, q in self.itens]

    def valor_total(self):
        total = 0.0
        for p, q in self.itens:
            total += p.preco * q
        return total

    def __repr__(self):
        return f"Pedido(itens={self.itens})"
