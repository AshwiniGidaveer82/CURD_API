# app/config.py

import os

class Settings:
    APP_NAME: str = "Book CRUD Microservice"
    HOST: str = os.environ.get("HOST", "0.0.0.0")
    PORT: int = int(os.environ.get("PORT", 8000))

settings = Settings()