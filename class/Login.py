class Login:
    def __init__(self):
        self.users = []

    def login(self, username, password, doc):
        for user in self.users:
            if user["Document"] == doc and user["Username"] == username and user["Password"] == password:
                return True
        return False