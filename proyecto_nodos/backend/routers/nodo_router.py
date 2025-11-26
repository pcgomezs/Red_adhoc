from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas
from ..database import get_db
from .. import crud

router = APIRouter(
    prefix="/nodo",
    tags=["Nodos"]
)

@router.get("/{nodo_id}")
def obtener_datos(nodo_id: int, db: Session = Depends(get_db)):
    return crud.get_datos_nodo(db, nodo_id)

@router.post("/registro/")
def crear_registro(registro: schemas.RegistroCreate, db: Session = Depends(get_db)):
    return crud.crear_registro(db, registro)

