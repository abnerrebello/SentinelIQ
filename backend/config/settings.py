from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str
    VERSION: str
    DEBUG: bool

    DATABASE_URL: str

    SECRET_KEY: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    UPLOAD_FOLDER: str

    MAX_UPLOAD_SIZE: int

    class Config:
        env_file = ".env"


settings = Settings()