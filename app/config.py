"""import os
from dotenv import load_dotenv

# Load values from a .env file if present (handy for local dev)
load_dotenv()

class Settings:
    APP_HOST: str = os.getenv("APP_HOST", "localhost")
    APP_PORT: int = int(os.getenv("APP_PORT", "8080"))
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./books.db")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"""