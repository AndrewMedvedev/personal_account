__all__ = (
    "router_answer",
    "router_get_token",
    "router_logout",
    "router_predict",
    "router_visitors",
    "router_vk",
    "router_yandex",
)

from src.routers.answer import router_answer
from src.routers.get_token import router_get_token
from src.routers.logout import router_logout
from src.routers.predict import router_predict
from src.routers.visitors import router_visitors
from src.routers.vk import router_vk
from src.routers.yandex import router_yandex
