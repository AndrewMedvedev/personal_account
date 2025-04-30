from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from ..constants import PATH_ENDPOINT
from ..lifespan import broker
from ..schemas import AssistantMessage, UserMessage
from ..utils import connection_manager

wb = APIRouter(prefix=f"{PATH_ENDPOINT}websocket", tags=["websocket"])


@wb.websocket("/{chat_id}")
async def chat(websocket: WebSocket, chat_id: str) -> None:
    await connection_manager.connect(websocket=websocket, chat_id=chat_id)
    await broker.connect()
    try:
        while True:
            message = await websocket.receive_json()
            user_message = UserMessage.model_validate(message)
            await broker.publish(
                user_message, queue="chat.user-message", reply_to="chat.assistant-message"
            )
    except WebSocketDisconnect:
        await connection_manager.disconnect(chat_id=chat_id)


@broker.subscriber("chat.assistant-messages")
async def answer(assistant_message: AssistantMessage) -> None:
    await connection_manager.send(assistant_message.chat_id, assistant_message)
