# ...existing code...
# Demonstrações / Testes rápidos
# ============================

# Exercício 1 — funções de estoque
estoque: dict = {}  # estrutura: {nome: {"quantidade": int, "preco": float}}

def adicionar_estoque(nome: str, quantidade: int, preco: float = 0.0) -> None:
    q = int(quantidade)
    p = float(preco)
    if nome in estoque:
        estoque[nome]["quantidade"] += q
        estoque[nome]["preco"] = p
    else:
        estoque[nome] = {"quantidade": q, "preco": p}

def remover_estoque(nome: str, quantidade: int) -> None:
    q = int(quantidade)
    if nome not in estoque:
        raise KeyError(f"Produto {nome} não encontrado no estoque")
    if estoque[nome]["quantidade"] < q:
        raise ValueError(f"Quantidade insuficiente de {nome} no estoque")
    estoque[nome]["quantidade"] -= q
    if estoque[nome]["quantidade"] == 0:
        del estoque[nome]

def valor_total(nome: str) -> float:
    if nome not in estoque:
        raise KeyError(f"Produto {nome} não encontrado no estoque")
    return estoque[nome]["quantidade"] * estoque[nome]["preco"]


# Exercício 2 — classe Produto
class Produto:
    def __init__(self, nome: str, quantidade: int, preco: float):
        self.nome = nome
        self.quantidade = int(quantidade)
        self.preco = float(preco)

    def adicionar(self, q: int) -> None:
        self.quantidade += int(q)

    def remover(self, q: int) -> None:
        q = int(q)
        if q > self.quantidade:
            raise ValueError("Quantidade insuficiente no produto")
        self.quantidade -= q

    def valor_total(self) -> float:
        return self.quantidade * self.preco

    def __repr__(self) -> str:
        return f"Produto(nome={self.nome!r}, quantidade={self.quantidade}, preco={self.preco:.2f})"


# Exercício 3 — classe Usuario
class Usuario:
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self._senha = senha

    def autenticar(self, email: str, senha: str) -> bool:
        return self.email == email and self._senha == senha

    def __repr__(self) -> str:
        return f"Usuario(nome={self.nome!r}, email={self.email!r})"


# Exercício 4 — classe Pedido
class Pedido:
    def __init__(self):
        self.itens: list = []  # lista de tuplas (Produto, quantidade)

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


# Exercício 5 — classe Jogador
class Jogador:
    def __init__(self, nome: str, saldo: float = 0.0):
        self.nome = nome
        self.saldo = float(saldo)
        self.inventario: list = []

    def adicionar_saldo(self, valor: float) -> None:
        self.saldo += float(valor)

    def comprar_item(self, nome_item: str, preco: float) -> bool:
        preco = float(preco)
        if preco > self.saldo:
            raise ValueError("Saldo insuficiente para compra")
        self.saldo -= preco
        self.inventario.append((nome_item, preco))
        return True

    def __repr__(self) -> str:
        return f"Jogador(nome={self.nome!r}, saldo={self.saldo:.2f}, inventario={self.inventario})"


# Exercício 6 — classe Pagamento (compatível com Jogador/Usuario)
class Pagamento:
    def __init__(self, usuario, valor: float):
        self.usuario = usuario
        self.valor = float(valor)
        self.status = "pendente"

    def processar(self) -> bool:
        if self.valor <= 0:
            self.status = "falha"
            return False
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


# Exercício 7 — Biblioteca e Livro
class Livro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False

    def __repr__(self) -> str:
        return f"Livro(titulo={self.titulo!r}, autor={self.autor!r}, emprestado={self.emprestado})"

class Biblioteca:
    def __init__(self):
        self.livros: list[Livro] = []

    def adicionar_livro(self, livro: Livro) -> None:
        self.livros.append(livro)

    def listar_disponiveis(self) -> list[str]:
        return [l.titulo for l in self.livros if not l.emprestado]

    def emprestar_livro(self, titulo: str) -> None:
        for l in self.livros:
            if l.titulo == titulo:
                if l.emprestado:
                    raise Exception(f"Livro '{titulo}' já está emprestado")
                l.emprestado = True
                return
        raise Exception(f"Livro '{titulo}' não encontrado")


# Exercício 8 — Funcionario
class Funcionario:
    def __init__(self, nome: str, cargo: str, salario: float):
        self.nome = nome
        self.cargo = cargo
        self.salario = float(salario)

    def aumentar_salario(self, percentual: float) -> None:
        self.salario *= (1 + float(percentual) / 100.0)

    def __repr__(self) -> str:
        return f"Funcionario(nome={self.nome!r}, cargo={self.cargo!r}, salario={self.salario:.2f})"


# Demo (já existente no arquivo original)
def demo():
    print("=== Exercício 1 (funções) ===")
    adicionar_estoque("Caneta", 10, preco=1.5)
    adicionar_estoque("Lápis", 5, preco=0.8)
    print("Estoque:", estoque)
    print("Valor total Caneta:", valor_total("Caneta"))
    remover_estoque("Caneta", 2)
    print("Após remover 2 canetas:", estoque.get("Caneta"))

    print("\n=== Exercício 2 (POO Produto) ===")
    p = Produto("Caderno", 20, 8.50)
    print(p)
    p.adicionar(5)
    p.remover(3)
    print("Valor total caderno:", p.valor_total())

    print("\n=== Exercício 3 (Usuario) ===")
    u1 = Usuario("Alice", "alice@example.com", "senha123")
    u2 = Usuario("Bob", "bob@example.com", "qwerty")
    print("Autentica Alice (correto):", u1.autenticar("alice@example.com", "senha123"))
    print("Autentica Bob (incorreto):", u2.autenticar("bob@example.com", "senhaErrada"))

    print("\n=== Exercício 4 (Pedido) ===")
    prod1 = Produto("Teclado", 10, 120.0)
    prod2 = Produto("Mouse", 20, 45.0)
    pedido = Pedido()
    pedido.adicionar_produto(prod1, 1)
    pedido.adicionar_produto(prod2, 2)
    print("Itens do pedido:", pedido.listar_produtos())
    print("Total do pedido:", pedido.valor_total())

    print("\n=== Exercício 5 (Jogador) ===")
    j = Jogador("Guilherme", saldo=50.0)
    print(j)
    j.adicionar_saldo(25.0)
    j.comprar_item("Espada", 30.0)
    print("Após compra:", j)

    print("\n=== Exercício 6 (Pagamento) ===")
    pag = Pagamento(j, 40.0)
    pag.processar()
    print("Pagamento:", pag)
    print("Saldo do jogador após pagamento:", j.saldo)

    print("\n=== Exercício 7 (Biblioteca) ===")
    b = Biblioteca()
    l1 = Livro("Dom Casmurro", "Machado de Assis")
    l2 = Livro("1984", "George Orwell")
    b.adicionar_livro(l1)
    b.adicionar_livro(l2)
    print("Disponíveis:", b.listar_disponiveis())
    b.emprestar_livro("1984")
    print("Após emprestar 1984, disponíveis:", b.listar_disponiveis())
    try:
        b.emprestar_livro("1984")
    except Exception as e:
        print("Erro ao emprestar novamente (esperado):", e)

    print("\n=== Exercício 8 (Funcionario) ===")
    f = Funcionario("Mariana", "Analista", 4500.0)
    print(f)
    f.aumentar_salario(10)
    print("Após aumento 10%:", f)

if __name__ == "__main__":
    demo()
