from ..rest import AnswerApi


class AnswerControl:
    def __init__(self):
        self.answer_api = AnswerApi()

    async def answer(self, message: str) -> dict:
        return await self.answer_api.get_anwer(message=message)
