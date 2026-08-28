class Registrar:
    def init__(self):
        self.users = []

    def register(self, username, password, doc):
        for user in self.users:
            if user["Document"] == doc:
                return False

        self.users.append({
            "Username": username,
            "Password": password,
            "Document": doc
        })