from sqlalchemy import create_engine, Column, Integer, String

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    document = Column(String)
