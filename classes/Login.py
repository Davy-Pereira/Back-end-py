from Database.Banco import Banco
from http import HTTPStatus

class Login:
    def __init__(self, banco: Banco):
        self.banco = banco

    def autenticar(self, username: str, password: str, doc: int) -> bool:
        usuario = self.banco.buscar_usuarios(
            username,
            password,
            doc
        )

        if usuario:
            return True
        raise HTTPStatus.UNAUTHORIZED("Credenciais inválidas.")