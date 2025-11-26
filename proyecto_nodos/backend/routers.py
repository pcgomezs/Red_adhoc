from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import crud, schemas, models
from .database import get_db

router = APIRouter()

# Crear registro
@router.post("/registro")
def crear_registro_api(registro: schemas.RegistroCreate, db: Session = Depends(get_db)):
    return crud.crear_registro(db, registro)

# Obtener datos por nodo
@router.get("/nodo/{nodo}")
def get_nodo_data(nodo: int, db: Session = Depends(get_db)):
    return db.query(models.Registro).filter(models.Registro.nodo == nodo).all()
