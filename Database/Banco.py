from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base, Session

Base = declarative_base()
Base.metadata.bind = create_engine('sqlite:///usuarios.db', echo=True)

engine = create_engine('sqlite:///usuarios.db', echo=True)
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    Username = Column(String)
    Password = Column(String)
    Document = Column(Integer)


Base.metadata.create_all(engine)

class Banco:
    def __init__(self):
        self.engine = engine

    def adicionar_usuario(self, username: str, password: str, document: int):
        with Session(self.engine) as session:
            novo_usuario = Usuario(Username=username, Password=password, Document=document)
            session.add(novo_usuario)
            session.commit()

    def buscar_usuarios(self, username: str, password: str, document: int):
        with Session(self.engine) as session:
            usuario = session.query(Usuario).filter_by(
                username=username,
                password=password,
                document=document
            ).first()
        return usuario