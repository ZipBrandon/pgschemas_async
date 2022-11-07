from typing import Optional

from django_pgschemas import get_current_schema
from strawberry import ID
from strawberry_django_plus import gql

from clients.models import Client


@gql.django.type(Client)
class ClientType:
    id: ID
    name: str
    current_schema: str


@gql.type
class Query:
    @gql.field()
    async def get_client(
        self,
        info,
    ) -> Optional[ClientType]:

        current_schema = get_current_schema().schema_name
        context_tenant = info.context.request.tenant

        return ClientType(
            id=context_tenant.id,
            name=context_tenant.name,
            current_schema=current_schema,
        )

    @gql.field()
    def get_client_sync(
        self,
        info,
    ) -> Optional[ClientType]:

        current_schema = get_current_schema().schema_name
        context_tenant = info.context.request.tenant

        return ClientType(
            id=context_tenant.id,
            name=context_tenant.name,
            current_schema=current_schema,
        )
