from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    MONGO_CONNECTION_STRING: str
    MONGO_DB_NAME: str
    
    # Configuración de la aplicación
    APP_NAME: str = Field(
        default="API del Proyecto SIGEU", 
        description="Sistema Gestion Eventos Universitarios"
    )
    APP_VERSION: str = Field(
        default="1.0.0", 
        description="Versión de la aplicación"
    )
    
    # Configuración de CORS
    ALLOWED_ORIGINS: List[str] = Field(
        default=["*"], 
        description="Orígenes permitidos para CORS"
    )
    
settings = Settings()
