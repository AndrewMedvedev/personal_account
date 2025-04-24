from ..rest import NewsApi


class NewsControl:
    def __init__(self):
        self.news_api = NewsApi()

    async def get_news(self, page: int, limit: int) -> dict:
        return await self.news_api.get_news(page=page, limit=limit)
