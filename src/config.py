from dotenv import dotenv_values, find_dotenv

env_path = find_dotenv()


config = dotenv_values(env_path)


class Settings:
    RECOMENDATE: str = config["RECOMENDATE"]
    DIRECTION: str = config["DIRECTION"]
    POINTS: str = config["POINTS"]
    EXAMS: str = config["EXAMS"]
    CLASSIFIER: str = config["CLASSIFIER"]
    CLASSIFIER_FREE: str = config["CLASSIFIER_FREE"]
    VALIDATE_ACCESS: str = config["VALIDATE_ACCESS"]
    VALIDATE_REFRESH: str = config["VALIDATE_REFRESH"]
    RAG_GigaChat_API: str = config["RAG_GigaChat_API"]

    VISITORS_ADD: str = config["VISITORS_ADD"]
    VISITORS_DELETE: str = config["VISITORS_DELETE"]
    VISITORS_GET: str = config["VISITORS_GET"]

    EVENTS_GET: str = config["EVENTS_GET"]

    NEWS_GET: str = config["NEWS_GET"]

    VK_APP_ID: int = config["VK_APP_ID"]
    VK_APP_SECRET: str = config["VK_APP_SECRET"]
    VK_REDIRECT_URI: str = config["VK_REDIRECT_URI"]
    VK_AUTH_URL: str = config["VK_AUTH_URL"]
    VK_TOKEN_URL: str = config["VK_TOKEN_URL"]
    VK_API_URL: str = config["VK_API_URL"]
    STATE_VK: str = config["STATE_VK"]
    CLIENT_SECRET: str = config["CLIENT_SECRET"]

    YANDEX_APP_ID: str = config["YANDEX_APP_ID"]
    YANDEX_APP_SECRET: str = config["YANDEX_APP_SECRET"]
    YANDEX_REDIRECT_URI: str = config["YANDEX_REDIRECT_URI"]
    YANDEX_AUTH_URL: str = config["YANDEX_AUTH_URL"]
    YANDEX_TOKEN_URL: str = config["YANDEX_TOKEN_URL"]
    YANDEX_API_URL: str = config["YANDEX_API_URL"]
    STATE_YANDEX: str = config["STATE_YANDEX"]
    YANDEX_SCOPE: str = config["YANDEX_SCOPE"]

    REGISTRATION_VK: str = config["REGISTRATION_VK"]
    REGISTRATION_YANDEX: str = config["REGISTRATION_YANDEX"]


settings = Settings()
