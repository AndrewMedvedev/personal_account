__all__ = (
    "router_answer",
    "router_set_token",
    "router_logout",
    "router_predict",
    "router_visitors",
    "router_vk",
    "router_yandex",
)

from .answer import router_answer
from .logout import router_logout
from .predict import router_predict
from .set_token import router_set_token
from .visitors import router_visitors
from .vk import router_vk
from .yandex import router_yandex
