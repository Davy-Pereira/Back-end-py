from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Base.metadata.bind = create_engine('sqlite:///usuarios.db', echo=True)
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    document = Column(Integer)
