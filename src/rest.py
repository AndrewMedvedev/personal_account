from uuid import UUID

from aiohttp import ClientSession

from config import settings

from .baseclasses import BaseAPI
from .schemas import PredictSchema
from .utils import valid_answer


class RegistrationApi:
    async def registration_vk(params: dict) -> None:
        async with (
            ClientSession() as session,
            session.post(url=settings.REGISTRATION_VK, json=params, ssl=False) as data,
        ):
            return await valid_answer(response=data)

    async def registration_yandex(params: dict) -> None:
        async with (
            ClientSession() as session,
            session.post(url=settings.REGISTRATION_YANDEX, json=params, ssl=False) as data,
        ):
            return await valid_answer(response=data)


class VKApi(BaseAPI):
    async def get_token(self, params: dict) -> dict:
        async with (
            ClientSession() as session,
            session.post(url=settings.VK_TOKEN_URL, json=params, ssl=False) as data,
        ):
            self.logger.warning(data)
            return await valid_answer(response=data)

    async def get_data(self, params: dict) -> dict:
        async with (
            ClientSession() as session,
            session.post(url=settings.VK_API_URL, json=params, ssl=False) as data,
        ):
            self.logger.warning(data)
            return await valid_answer(response=data)


class YandexApi(BaseAPI):
    async def get_token(self, params: dict) -> dict:
        async with (
            ClientSession() as session,
            session.post(url=settings.YANDEX_TOKEN_URL, data=params, ssl=False) as data,
        ):
            self.logger.warning(data)
            return await valid_answer(response=data)

    async def get_data(self, params: dict) -> dict:
        async with (
            ClientSession() as session,
            session.get(url=settings.YANDEX_API_URL, params=params, ssl=False) as data,
        ):
            self.logger.warning(data)
            return await valid_answer(response=data)


class PredictApi(BaseAPI):
    async def get_data_recomendate(
        self,
        data: dict,
    ) -> dict:
        async with (
            ClientSession() as session,
            session.post(
                settings.RECOMENDATE,
                json=data,
                ssl=False,
            ) as resp,
        ):
            self.logger.warning(resp)
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
            ClientSession() as session,
            session.post(
                url=settings.CLASSIFIER,
                json=correct_data,
                ssl=False,
            ) as resp,
        ):
            self.logger.warning(resp)
            return (await valid_answer(resp))["probabilities"]

    async def get_data_classifier_applicant(
        self,
        data: dict,
    ) -> float:
        async with (
            ClientSession() as session,
            session.post(
                url=settings.CLASSIFIER_FREE,
                json=data,
                ssl=False,
            ) as resp,
        ):
            self.logger.warning(resp)
            return (await valid_answer(resp))["probability"]

    async def get_data_directions(
        self,
        direction_id: int,
    ) -> dict:
        async with (
            ClientSession() as session,
            session.get(
                url=f"{settings.DIRECTION}{direction_id}",
                ssl=False,
            ) as data,
        ):
            self.logger.warning(data)
            return (await valid_answer(data))["description"]

    async def get_data_points(
        self,
        direction_id: int,
    ) -> dict:
        async with (
            ClientSession() as session,
            session.get(
                url=f"{settings.POINTS}{direction_id}",
                ssl=False,
            ) as data,
        ):
            self.logger.warning(data)
            return (await valid_answer(data))["history"]

    async def get_data_exams(
        self,
        direction_id: int,
    ) -> dict:
        async with (
            ClientSession() as session,
            session.get(
                url=f"{settings.EXAMS}{direction_id}",
                ssl=False,
            ) as data,
        ):
            self.logger.warning(data)
            return (await valid_answer(data))["entrance_exams"]


class EventApi(BaseAPI):
    async def get_events(self, page: int, limit: int) -> dict:
        async with (
            ClientSession() as session,
            session.get(
                url=settings.EVENTS_GET,
                params={
                    "is_paginated": "true",
                    "page": page,
                    "limit": limit,
                },
                ssl=False,
            ) as data,
        ):
            self.logger.warning(data)
            return await valid_answer(data)


class NewsApi(BaseAPI):
    async def get_news(self, page: int, limit: int) -> dict:
        async with (
            ClientSession() as session,
            session.get(
                url=settings.NEWS_GET,
                params={
                    "is_paginated": "true",
                    "page": page,
                    "limit": limit,
                },
                ssl=False,
            ) as data,
        ):
            self.logger.warning(data)
            return await valid_answer(data)


class VisitorApi(BaseAPI):
    async def visitor_create(
        self,
        event_id: int,
        user_id: UUID,
    ) -> dict:
        async with (
            ClientSession() as session,
            session.post(
                url=f"{settings.VISITORS_ADD}{event_id}/{user_id}",
                ssl=False,
            ) as data,
        ):
            self.logger.warning(data)
            return await valid_answer(data)

    async def visitor_get(
        self,
        user_id: UUID,
    ) -> dict:
        async with (
            ClientSession() as session,
            session.get(
                url=f"{settings.VISITORS_GET}{user_id}",
                ssl=False,
            ) as data,
        ):
            self.logger.warning(data)
            return await valid_answer(data)

    async def visitor_delete(
        self,
        event_id: int,
        user_id: UUID,
    ) -> dict:
        async with (
            ClientSession() as session,
            session.delete(
                url=f"{settings.VISITORS_DELETE}{event_id}/{user_id}",
                ssl=False,
            ) as data,
        ):
            self.logger.warning(data)
            return await valid_answer(data)


class AnswerApi(BaseAPI):
    async def get_anwer(self, message: str) -> dict:
        async with (
            ClientSession() as session,
            session.post(
                url=settings.RAG_GigaChat_API,
                json={"question": message},
                ssl=False,
            ) as data,
        ):
            self.logger.warning(data)
            return await valid_answer(data)
