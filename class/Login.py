from Database.Banco import Usuario, Base

Banco = Usuario(Base.metadata.bind)

class Login:
    def __init__(self, Banco):
        self.Banco = Banco

    def login(self, username, password, doc):
        for user in self.Banco.get_users():
            if user["Document"] == doc and user["Username"] == username and user["Password"] == password:
                return True
        self.Banco.add_user(username, password, doc)
