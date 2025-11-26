from sqlalchemy.orm import Session
from . import models, schemas

# Crear registro
def crear_registro(db: Session, registro: schemas.RegistroCreate):
    db_registro = models.Registro(
        nodo=registro.nodo,
        latitud=registro.latitud,
        longitud=registro.longitud,
        variable=registro.variable,
        dato=registro.dato
    )
    db.add(db_registro)
    db.commit()
    db.refresh(db_registro)
    return db_registro


# Obtener datos de un nodo específico
def get_datos_nodo(db: Session, nodo_id: int):
    return (
        db.query(models.Registro)
        .filter(models.Registro.nodo == nodo_id)
        .order_by(models.Registro.id.desc())
        .limit(1000)
        .all()
    )

def eliminar_por_nodo(db: Session, nodo_id: int):
    db.query(models.Registro).filter(models.Registro.nodo == nodo_id).delete()
    db.commit()
    return {"mensaje": f"Registros del nodo {nodo_id} eliminados."}
