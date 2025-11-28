# Exercício 1 — Funções soltas (registro de produtos)
estoque = {}  # chave: nome do produto -> dict {qtd, preco}

def adicionar_estoque(produto, qtd, preco=None):
    """
    Adiciona quantidade ao estoque. Se produto novo, cria com preco (se fornecido).
    """
    if produto not in estoque:
        if preco is None:
            raise ValueError("Produto novo requer preço.")
        estoque[produto] = {"qtd": 0, "preco": float(preco)}
    estoque[produto]["qtd"] += int(qtd)

def remover_estoque(produto, qtd):
    """
    Remove qtd do estoque se houver saldo.
    """
    if produto not in estoque:
        raise KeyError("Produto não existe no estoque.")
    if estoque[produto]["qtd"] < qtd:
        raise ValueError("Quantidade insuficiente.")
    estoque[produto]["qtd"] -= int(qtd)

def valor_total(produto):
    """
    Retorna valor total (qtd * preco) de um produto.
    """
    if produto not in estoque:
        raise KeyError("Produto não existe no estoque.")
    return estoque[produto]["qtd"] * estoque[produto]["preco"]