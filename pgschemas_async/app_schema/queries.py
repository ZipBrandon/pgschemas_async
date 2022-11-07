from typing import Optional

from strawberry import ID
from strawberry_django_plus import gql

from clients.models import Client


@gql.django.type(Client)
class ClientType:
    id: ID
    name: str


@gql.type
class Query:
    @gql.field()
    def get_client(self, info, client_id: Optional[ID] = None) -> Optional[ClientType]:
        if not client_id:
            return info.context.request.tenant
        qs = Client.objects.filter(id=client_id).first()
        return qs
