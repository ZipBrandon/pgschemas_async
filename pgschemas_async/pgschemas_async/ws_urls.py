from django.urls import re_path
from strawberry.channels.handlers.ws_handler import GraphQLWSConsumer
from app_schema.schema import schema

from pgschemas_async import routing

gql_ws_consumer = GraphQLWSConsumer.as_asgi(schema=schema)

urlpatterns = routing.websocket_urlpatterns + [
    re_path(r"graphql/?", gql_ws_consumer),
]
