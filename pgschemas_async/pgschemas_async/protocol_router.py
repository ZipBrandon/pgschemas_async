from channels.db import database_sync_to_async
from channels.routing import URLRouter
from django_pgschemas import activate
from django_pgschemas.contrib.channels3 import TenantProtocolRouter
from django_pgschemas.contrib.channels3.auth import TenantAuthMiddlewareStack
from django_pgschemas.contrib.channels3.router import TenantAwareProtocolTypeRouter


class MyTenantProtocolRouter(TenantProtocolRouter):
    """
    ProtocolRouter that handles multi-tenancy.
    """

    http = None

    def __init__(self, http, **kwargs):
        self.http = http
        super().__init__()

    def get_protocol_type_router(self, tenant_prefix, ws_urlconf):
        """
        Subclasses can override this to include more protocols.
        """
        return TenantAwareProtocolTypeRouter(
            {
                "http": self.http,
                "websocket": TenantAuthMiddlewareStack(URLRouter(ws_urlconf)),
            },
            tenant_prefix,
        )
