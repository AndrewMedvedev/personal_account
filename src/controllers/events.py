from ..rest import EventApi


class EventControl:
    def __init__(self):
        self.event_api = EventApi()

    async def get_events(self, page: int, limit: int) -> dict:
        return await self.event_api.get_events(page=page, limit=limit)
