import strawberry
from strawberry.types import Info

from app_schema.types import ChatRoom


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def send_chat_message(
        self,
        info: Info,
        room: ChatRoom,
        message: str,
    ) -> None:

        ws = info.context.ws
        channel_layer = ws.channel_layer

        await channel_layer.group_send(
            f"chat_{room.room_name}",
            {
                "type": "chat.message",
                "room_id": room.room_name,
                "message": message,
            },
        )
