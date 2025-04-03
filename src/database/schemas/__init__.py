__all__ = (
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


from .predict_schemas import PredictFree, PredictModel
from .vk_schemas import (DictGetDataTokenVK, DictGetDataVK, DictLinkVK,
                         RegistrationVK)
from .yandex_schemas import (DictGetDataTokenYandex, DictGetDataYandex,
                             DictLinkYandex, RegistrationYandex)
