__all__ = (
    "DictGetDataTokenVK",
    "DictGetDataTokenYandex",
    "DictGetDataVK",
    "DictGetDataYandex",
    "DictLinkVK",
    "DictLinkYandex",
    "PredictFree",
    "PredictModel",
    "RegistrationVK",
    "RegistrationYandex",
)


from .predict_schemas import PredictFree, PredictModel
from .vk_schemas import DictGetDataTokenVK, DictGetDataVK, DictLinkVK, RegistrationVK
from .yandex_schemas import (
    DictGetDataTokenYandex,
    DictGetDataYandex,
    DictLinkYandex,
    RegistrationYandex,
)
