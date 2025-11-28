# Exercício 3 — Cadastro de Usuários
class Usuario:
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self._senha = senha  # em projeto real: nunca armazenar em plain-text

    def autenticar(self, email: str, senha: str) -> bool:
        return self.email == email and self._senha == senha

    def __repr__(self):
        return f"Usuario(nome={self.nome!r}, email={self.email!r})"