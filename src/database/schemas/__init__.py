__all__ = (
    "DictGetDataVK",
    "DictGetDataTokenVK",
    "DictLinkVK",
    "DictGetDataYandex",
    "DictGetDataTokenYandex",
    "DictLinkYandex",
    "PredictFree",
    "PredictModel",
)

from src.database.schemas.predict_schemas import PredictFree, PredictModel
from src.database.schemas.vk_schemas import (DictGetDataTokenVK, DictGetDataVK,
                                             DictLinkVK)
from src.database.schemas.yandex_schemas import (DictGetDataTokenYandex,
                                                 DictGetDataYandex,
                                                 DictLinkYandex)
