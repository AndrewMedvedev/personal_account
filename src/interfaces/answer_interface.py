from abc import ABC, abstractmethod


class AnswerBase(ABC):

    @abstractmethod
    async def get_answer(self) -> dict:
        raise NotImplementedError