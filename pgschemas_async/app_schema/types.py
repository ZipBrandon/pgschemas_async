import strawberry


@strawberry.input
class ChatRoom:
    room_name: str


@strawberry.type
class ChatRoomMessage:
    room_name: str
    current_user: str
    message: str
