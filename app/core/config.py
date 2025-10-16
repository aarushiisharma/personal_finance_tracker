from pydantic import BaseSettings

class Settings(BaseSettings):
    mongo_uri: str
    mongo_db: str
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
