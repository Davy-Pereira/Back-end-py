from Database.Banco import Banco
from Interface.main import Interface

db = Banco()

interface = Interface(db)
interface.executar()