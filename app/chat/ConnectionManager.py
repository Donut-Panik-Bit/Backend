from typing import List
from fastapi import WebSocket
from app.schemas.chat import Chat


class ConnectionManager:
    def __init__(self) -> None:
        self.active_connections: List[(WebSocket, str)] = []
        self.neew_help_conn: List[(WebSocket, str)] = []

    async def connect(self, websocket: WebSocket, nickname: str) -> None:
        await websocket.accept()
        self.active_connections.append((websocket, nickname))
        self.neew_help_conn.append((websocket, nickname))

    def disconnect(self, websocket: WebSocket, nickname: str) -> None:
        self.active_connections.remove((websocket, nickname))

    async def send_personal_message(self, message: str, websocket: WebSocket) -> None:
        await websocket.send_text(message)

    async def broadcast(self, message: str) -> None:
        for connection in self.active_connections:
            await connection[0].send_text(message)

    async def get_chats_with_promlem(self):
        chats: List[Chat] = []
        for chat in self.neew_help_conn:
            chats.append(Chat(name=str(chat[1]), status=chat[0].client_state.name))
        return chats
