import asyncio
import os
import threading
from typing import AsyncGenerator, List

import strawberry
from strawberry import subscription
from strawberry.types import Info

from app_schema.types import ChatRoom, ChatRoomMessage


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(self, target: int = 100) -> AsyncGenerator[int, None]:
        for i in range(target):
            yield i
            await asyncio.sleep(0.5)

    @strawberry.subscription
    async def join_chat_rooms(
        self,
        info: Info,
        rooms: List[ChatRoom],
        user: str,
    ) -> AsyncGenerator[ChatRoomMessage, None]:
        """Join and subscribe to message sent to the given rooms."""
        ws = info.context.ws
        channel_layer = ws.channel_layer

        room_ids = [f"chat_{room.room_name}" for room in rooms]

        for room in room_ids:
            # Join room group
            await channel_layer.group_add(room, ws.channel_name)

        for room in room_ids:
            await channel_layer.group_send(
                room,
                {
                    "type": "chat.message",
                    "room_id": room,
                    "message": f"process: {os.getpid()} thread: {threading.current_thread().name}"
                    f" -> Hello my name is {user}!",
                },
            )

        async for message in ws.channel_listen("chat.message", groups=room_ids):
            yield ChatRoomMessage(
                room_name=message["room_id"],
                message=message["message"],
                current_user=user,
            )
