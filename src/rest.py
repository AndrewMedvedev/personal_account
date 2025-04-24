from aiohttp import ClientSession

from config import Settings

from .schemas import PredictSchema
from .utils import valid_answer


class BaseApi:
    def __init__(self):
        self.settings = Settings
        self.clientsession = ClientSession


class RegistrationApi(BaseApi):
    async def registration_vk(self, params: dict) -> None:
        async with (
            self.clientsession() as session,
            session.post(url=Settings.REGISTRATION_VK, json=params, ssl=False) as data,
        ):
            return await valid_answer(response=data)

    async def registration_yandex(self, params: dict) -> None:
        async with (
            self.clientsession() as session,
            session.post(url=Settings.REGISTRATION_YANDEX, json=params, ssl=False) as data,
        ):
            return await valid_answer(response=data)


class VKApi(BaseApi):
    async def get_token(self, params: dict) -> dict:
        async with (
            self.clientsession() as session,
            session.post(url=Settings.VK_TOKEN_URL, json=params, ssl=False) as data,
        ):
            return await valid_answer(response=data)

    async def get_data(self, params: dict) -> dict:
        async with (
            self.clientsession() as session,
            session.post(url=Settings.VK_API_URL, json=params, ssl=False) as data,
        ):
            return await valid_answer(response=data)


class YandexApi(BaseApi):
    async def get_token(self, params: dict) -> dict:
        async with (
            self.clientsession() as session,
            session.post(url=Settings.YANDEX_TOKEN_URL, data=params, ssl=False) as data,
        ):
            return await valid_answer(response=data)

    async def get_data(self, params: dict) -> dict:
        async with (
            self.clientsession() as session,
            session.get(url=Settings.YANDEX_API_URL, params=params, ssl=False) as data,
        ):
            return await valid_answer(response=data)


class PredictApi(BaseApi):
    async def get_data_recomendate(
        self,
        data: dict,
    ) -> dict:
        async with (
            self.clientsession() as session,
            session.post(
                self.settings.RECOMENDATE,
                json=data,
                ssl=False,
            ) as resp,
        ):
            return (await valid_answer(resp))["directions"]

    async def get_data_classifier_applicants(
        self,
        data: PredictSchema,
        directions: list,
    ) -> dict:
        correct_data = {
            "applicants": [
                data.to_dict_get_data_classifier_applicants(direction=str(i.get("name")))
                for i in directions
            ]
        }
        async with (
            self.clientsession() as session,
            session.post(
                url=self.settings.CLASSIFIER,
                json=correct_data,
                ssl=False,
            ) as resp,
        ):
            return (await valid_answer(resp))["probabilities"]

    async def get_data_classifier_applicant(
        self,
        data: dict,
    ) -> float:
        async with (
            self.clientsession() as session,
            session.post(
                url=f"{self.settings.CLASSIFIER_FREE}",
                json=data,
                ssl=False,
            ) as resp,
        ):
            return (await valid_answer(resp))["probability"]

    async def get_data_directions(
        self,
        direction_id: int,
    ) -> dict:
        async with (
            self.clientsession() as session,
            session.get(
                url=f"{self.settings.DIRECTION}{direction_id}",
                ssl=False,
            ) as data,
        ):
            return (await valid_answer(data))["description"]

    async def get_data_points(
        self,
        direction_id: int,
    ) -> dict:
        async with (
            self.clientsession() as session,
            session.get(
                url=f"{self.settings.POINTS}{direction_id}",
                ssl=False,
            ) as data,
        ):
            return (await valid_answer(data))["history"]

    async def get_data_exams(
        self,
        direction_id: int,
    ) -> dict:
        async with (
            self.clientsession() as session,
            session.get(
                url=f"{self.settings.EXAMS}{direction_id}",
                ssl=False,
            ) as data,
        ):
            return (await valid_answer(data))["entrance_exams"]


class EventApi(BaseApi):
    async def get_events(self, page: int, limit: int) -> dict:
        async with (
            self.clientsession() as session,
            session.get(
                url=self.settings.EVENTS_GET,
                params={
                    "is_paginated": "true",
                    "page": page,
                    "limit": limit,
                },
                ssl=False,
            ) as data,
        ):
            return await valid_answer(data)


class NewsApi(BaseApi):
    async def get_news(self, page: int, limit: int) -> dict:
        async with (
            self.clientsession() as session,
            session.get(
                url=self.settings.NEWS_GET,
                params={
                    "is_paginated": "true",
                    "page": page,
                    "limit": limit,
                },
                ssl=False,
            ) as data,
        ):
            return await valid_answer(data)


class VisitorApi(BaseApi):
    async def visitor_create(
        self,
        event_id: int,
        user_id: int,
    ) -> dict:
        async with (
            self.clientsession() as session,
            session.post(
                url=f"{self.settings.VISITORS_ADD}{event_id}/{user_id}",
                ssl=False,
            ) as data,
        ):
            return await valid_answer(data)

    async def visitor_get(
        self,
        user_id: int,
    ) -> dict:
        async with (
            self.clientsession() as session,
            session.get(
                url=f"{self.settings.VISITORS_GET}{user_id}",
                ssl=False,
            ) as data,
        ):
            return await valid_answer(data)

    async def visitor_delete(
        self,
        event_id: int,
        user_id: int,
    ) -> dict:
        async with (
            self.clientsession() as session,
            session.delete(
                url=f"{self.settings.VISITORS_DELETE}{event_id}/{user_id}",
                ssl=False,
            ) as data,
        ):
            return await valid_answer(data)


class AnswerApi(BaseApi):
    async def get_anwer(self, message: str) -> dict:
        async with (
            self.clientsession() as session,
            session.post(
                url=self.settings.RAG_GigaChat_API,
                json={"question": message},
                ssl=False,
            ) as data,
        ):
            return await valid_answer(data)
