from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

from channels.db import database_sync_to_async
from strawberry.channels.handlers.base import ChannelsConsumer
from strawberry.channels.handlers.http_handler import (
    GraphQLHTTPConsumer,
    SyncGraphQLHTTPConsumer,
)
from strawberry.channels.handlers.ws_handler import GraphQLWSConsumer
from strawberry.http import (
    GraphQLHTTPResponse,
    GraphQLRequestData,
    process_result,
)
from strawberry.types import ExecutionResult
from strawberry.types.graphql import OperationType


if TYPE_CHECKING:
    from strawberry.channels.handlers.base import ChannelsConsumer
from clients.models import Client


@dataclass
class MyDjangoChannelsContext:
    """
    A Channels context for GraphQL
    """

    request: "ChannelsConsumer"
    tenant: Optional["Client"]

    @property
    def ws(self):
        return self.request


class MyGraphQLHTTPConsumer(GraphQLHTTPConsumer):
    tenant = None
    user = None
    host = None
    http_host = None
    session = None

    async def process_models(self, request):

        context = MyDjangoChannelsContext(
            request=request or self,
            tenant=self.tenant,
        )
        return context

    async def get_context(
        self,
        request: Optional["ChannelsConsumer"] = None,
    ) -> MyDjangoChannelsContext:
        self.tenant = self.scope.get("tenant")
        self.user = self.scope.get("user")
        self.host = self.scope.get("host")
        self.http_host = self.scope.get("http_host")
        self.session = self.scope.get("session")

        return await self.process_models(request)


class MySyncGraphQLHTTPConsumer(SyncGraphQLHTTPConsumer):
    tenant = None
    user = None
    host = None
    http_host = None
    session = None

    def process_models(self, request):

        context = MyDjangoChannelsContext(
            request=request or self,
            tenant=self.tenant,
        )
        return context

    def get_context(
        self,
        request: Optional["ChannelsConsumer"] = None,
    ) -> MyDjangoChannelsContext:
        self.tenant = self.scope.get("tenant")
        self.user = self.scope.get("user")
        self.host = self.scope.get("host")
        self.http_host = self.scope.get("http_host")
        self.session = self.scope.get("session")

        context = self.process_models(request)

        return context


class MyGraphQLWSConsumer(GraphQLWSConsumer):
    async def get_context(
        self,
        request: Optional["ChannelsConsumer"] = None,
    ) -> MyDjangoChannelsContext:
        tenant = None
        user = None
        host = None
        http_host = None
        session = None

        context = MyDjangoChannelsContext(
            request=request or self,
            tenant=self.tenant,
        )
        return context
