from dotenv import find_dotenv, dotenv_values


env_path = find_dotenv()


config = dotenv_values(env_path)


class Settings:
    DB_HOST: str = config["DB_HOST"]
    DB_PORT: int = config["DB_PORT"]
    DB_NAME: str = config["DB_NAME"]
    DB_USER: str = config["DB_USER"]
    DB_PASSWORD: str = config["DB_PASSWORD"]
    SECRET_KEY: str = config["SECRET_KEY"]
    ALGORITHM: str = config["ALGORITHM"]
    RECOMENDATE: str = config["RECOMENDATE"]
    CLASSIFIER: str = config["CLASSIFIER"]
    CLASSIFIER_FREE: str = config["CLASSIFIER_FREE"]
    VALIDATE_ACCESS: str = config["VALIDATE_ACCESS"]
    VALIDATE_REFRESH: str = config["VALIDATE_REFRESH"]
    RAG_GigaChat_API: str = config["RAG_GigaChat_API"]

settings = Settings()


def get_db_url():
    return (
        f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@"
        f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
    )
