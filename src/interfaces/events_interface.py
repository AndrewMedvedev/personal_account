from abc import ABC, abstractmethod


class EventsBase(ABC):

    @abstractmethod
    async def get_events() -> dict:
        raise NotImplementedError
