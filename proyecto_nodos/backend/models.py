
from sqlalchemy import Column, DateTime, Integer, String, Float, func
from .database import Base
from datetime import datetime

class Registro(Base):
    __tablename__ = "registros"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nodo = Column(Integer, index=True)   # Solo 4 nodos
    latitud = Column(Float)
    longitud = Column(Float)
    variable = Column(String)
    dato = Column(Float)
    fecha = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
