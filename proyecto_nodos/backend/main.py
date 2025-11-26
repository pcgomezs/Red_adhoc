import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

from . import models
from .database import engine
from .routers.nodo_router import router as nodo_router

models.Base.metadata.create_all(bind=engine)
load_dotenv()

app = FastAPI()

# OBTENER EL API
API_URL = os.getenv("API_URL")


#  CONFIGURA LOS CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#  API PRIMERO (IMPORTANTE)
app.include_router(nodo_router, prefix="/api")


#  FRONTEND DESPUÉS
BASE_DIR = os.path.dirname(os.path.abspath(__file__))          # .../backend
PROJECT_DIR = os.path.dirname(BASE_DIR)                        # .../proyecto_nodos
FRONTEND_DIR = os.path.join(PROJECT_DIR, "frontend")           # .../proyecto_nodos/frontend

print("FRONTEND_DIR:", FRONTEND_DIR)

# Montar frontend en la raíz "/"
app.mount(
    "/", 
    StaticFiles(directory=FRONTEND_DIR, html=True),
    name="frontend"
)
