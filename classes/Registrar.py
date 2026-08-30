from Database.Banco import Banco
from http import HTTPStatus

class Registrar:
    def __init__(self, banco: Banco):
        self.banco = banco

    def registrar(self, username: str, password: str, doc: int) -> bool:
        self.banco.adicionar_usuario(
            username, 
            password, 
            doc
        )
        return True