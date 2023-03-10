from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from app.auth.oauth2 import get_current_user
from app.chat import ConnectionManager
from app.query.auth import check_role
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.connection import get_session
from app.schemas.chat import Chat
from typing import List

from ..GranatHelper.GranatManager import GranatManager

chat_router = APIRouter(tags=["Chat"])


manager = ConnectionManager()


@chat_router.get("/ws/all", response_model=List[Chat])
async def websockets_pull(current_user: str = Depends(get_current_user),
                          session: AsyncSession = Depends(get_session)):
    # await check_role(current_user, session)
    return await manager.get_chats_with_promlem()


@chat_router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_text()
            answer = GranatManager.handle(msg=data)
            await manager.send_personal_message(answer, websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")
