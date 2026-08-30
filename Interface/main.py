import tkinter as tk
from tikinter import messagebox

from classes.Login import Login
from classes.Registrar import Registrar

class Interface:
    def __init__(self, banco):
        self.banco = banco
        self.login = Login(banco)
        self.registrar = Registrar(banco)
        self.root = tk.Tk()
        self.root.title("Sistema de Login")
        self.root.geometry("800x800")
        self.root.resizable(False, False)
        self.create_widgets()

    def fazer_login(self):
        resultado = self.login.autenticar(
            self.username.get(),
            self.password.get(),
            self.doc.get()
        )
        if resultado:
            messagebox.showinfo("Login", "Login bem-sucedido!")
        else:
            messagebox.showerror("Login", "Credenciais inválidas.")

    def executar(self):
        self.root.mainloop()