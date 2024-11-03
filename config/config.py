from dotenv import load_dotenv
import os

# Ładowanie zmiennych z pliku .env
load_dotenv()

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL")
    DEBUG = os.getenv("DEBUG") == "True"  # Konwertuje na wartość logiczną True lub False
    SECRET_KEY = os.getenv("SECRET_KEY")
