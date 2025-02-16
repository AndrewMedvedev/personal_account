from dotenv import dotenv_values, find_dotenv

env_path = find_dotenv()


config = dotenv_values(env_path)


class Settings:
    RECOMENDATE: str = config["RECOMENDATE"]
    CLASSIFIER: str = config["CLASSIFIER"]
    CLASSIFIER_FREE: str = config["CLASSIFIER_FREE"]
    VALIDATE_ACCESS: str = config["VALIDATE_ACCESS"]
    VALIDATE_REFRESH: str = config["VALIDATE_REFRESH"]
    RAG_GigaChat_API: str = config["RAG_GigaChat_API"]

settings = Settings()


