from dotenv import dotenv_values, find_dotenv

env_path = find_dotenv()


config = dotenv_values(env_path)


class Settings:
    RECOMENDATE: str = config["RECOMENDATE"]
    DIRECTION: str = config["DIRECTION"]
    DIRECTION_POINTS: str = config["DIRECTION_POINTS"]
    CLASSIFIER: str = config["CLASSIFIER"]
    CLASSIFIER_FREE: str = config["CLASSIFIER_FREE"]
    VALIDATE_ACCESS: str = config["VALIDATE_ACCESS"]
    VALIDATE_REFRESH: str = config["VALIDATE_REFRESH"]
    RAG_GigaChat_API: str = config["RAG_GigaChat_API"]

    VISITORS_ADD: str = config["VISITORS_ADD"]
    VISITORS_DELETE: str = config["VISITORS_DELETE"]
    VISITORS_GET: str = config["VISITORS_GET"]


settings = Settings()
