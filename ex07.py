# Exercício 7 — Sistema de Biblioteca
class Livro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if not self.disponivel:
            raise ValueError("Livro já emprestado.")
        self.disponivel = False

    def devolver(self):
        self.disponivel = True

    def __repr__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"Livro({self.titulo!r}, {self.autor!r}, {status})"

class Biblioteca:
    def __init__(self):
        self.livros = []  # lista de Livro

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)

    def emprestar_livro(self, titulo: str):
        for l in self.livros:
            if l.titulo == titulo:
                l.emprestar()
                return l
        raise LookupError("Livro não encontrado.")

    def devolver_livro(self, titulo: str):
        for l in self.livros:
            if l.titulo == titulo:
                l.devolver()
                return l
        raise LookupError("Livro não encontrado.")

    def listar_disponiveis(self):
        return [l for l in self.livros if l.disponivel]

    def __repr__(self):
        return f"Biblioteca({len(self.livros)} livros)"