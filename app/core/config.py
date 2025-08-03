import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "DataChat"
    SQLALCHEMY_DATABASE_URI: str = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

settings = Settings()