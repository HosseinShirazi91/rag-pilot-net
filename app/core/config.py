from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    env: str = "production"
    log_level: str = "INFO"

    postgres_host: str = "postgres"
    postgres_port: int = 5432
    postgres_user: str = "rag"
    postgres_password: str = "ragpass"
    postgres_db: str = "ragdb"

    jwt_secret: str = "change_me"
    jwt_expire_minutes: int = 1440

    qdrant_host: str = "qdrant"
    qdrant_port: int = 6333
    qdrant_api_key: str | None = None
    qdrant_collection: str = "regulations_chunks"

    embedding_model_name: str = "BAAI/bge-m3"
    ollama_host: str = "http://ollama:11434"
    ollama_model: str = "mistral-7b-instruct-q4"

    hf_home: str = "/hf_cache"

    class Config:
        env_prefix = ""
        case_sensitive = False

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()
