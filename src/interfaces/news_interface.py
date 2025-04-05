from abc import ABC, abstractmethod


class NewsBase(ABC):
    @abstractmethod
    async def get_news() -> dict:
        raise NotImplementedError
