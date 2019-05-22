from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class usuarios(connector.Manager.Base):
    __tablename__ = 'usuarios_'
    id = Column(Integer, Sequence('usuarios_id_seq'), primary_key=True)
    codigo = Column(Integer)
    nombre = Column(String(20))
    apellido = Column(String(20))
    password = Column(String(30))
