import datetime
from pydantic import BaseModel

class RegistroBase(BaseModel):
    nodo: int
    latitud: float
    longitud: float
    variable: str
    dato: float
    #fecha: datetime.datetime = None

class RegistroCreate(RegistroBase):
    pass

class RegistroOut(RegistroBase):
    id: int
    class Config:
        from_attributes: True  # reemplaza orm_mode=True
    