from dotenv import find_dotenv, dotenv_values


env_path = find_dotenv()


config = dotenv_values(env_path)


class Settings:
    SECRET_KEY: str = config["SECRET_KEY"]
    ALGORITHM: str = config["ALGORITHM"]
    RECOMENDATE: str = config["RECOMENDATE"]
    CLASSIFIER: str = config["CLASSIFIER"]
    CLASSIFIER_FREE: str = config["CLASSIFIER_FREE"]
    VALIDATE_ACCESS: str = config["VALIDATE_ACCESS"]
    VALIDATE_REFRESH: str = config["VALIDATE_REFRESH"]
    RAG_GigaChat_API: str = config["RAG_GigaChat_API"]

settings = Settings()


