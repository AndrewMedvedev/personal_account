__all__ = (
    "CustomResponse",
    "DictGetDataVK",
    "DictGetDataTokenVK",
    "DictLinkVK",
    "RegistrationVK",
    "DictGetDataYandex",
    "DictGetDataTokenYandex",
    "DictLinkYandex",
    "RegistrationYandex",
    "PredictFree",
    "PredictModel",
)

from .custom_response import CustomResponse
from .predict_schemas import PredictFree, PredictModel
from .vk_schemas import (DictGetDataTokenVK, DictGetDataVK, DictLinkVK,
                         RegistrationVK)
from .yandex_schemas import (DictGetDataTokenYandex, DictGetDataYandex,
                             DictLinkYandex, RegistrationYandex)
