from typing import Optional

from faststream.rabbit import RabbitBroker

from ..schemas import AssistantMessage, UserMessage


class ChatAssistantRabbitGateway:
    def __init__(self, broker: RabbitBroker) -> None:
        self._broker = broker

    async def answer(self, user_message: UserMessage) -> Optional[AssistantMessage]:
        return await self._broker.publish(
            user_message, queue="chat.user-message", reply_to="chat.assistant-message"
        )
