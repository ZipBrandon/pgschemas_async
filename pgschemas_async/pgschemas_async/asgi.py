"""
ASGI config for pgschemas_async project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""
import django

django.setup()


from pgschemas_async.context import MyGraphQLHTTPConsumer, MySyncGraphQLHTTPConsumer
from pgschemas_async.protocol_router import MyTenantProtocolRouter


import os

from django.urls import re_path

from app_schema.schema import schema

from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter
from django.core.asgi import get_asgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pgschemas_async.settings")


# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()


gql_http_sync_consumer = AuthMiddlewareStack(
    MySyncGraphQLHTTPConsumer.as_asgi(schema=schema)
)
gql_http_async_consumer = AuthMiddlewareStack(
    MyGraphQLHTTPConsumer.as_asgi(schema=schema)
)

application = MyTenantProtocolRouter(
    http=URLRouter(
        [
            re_path("^graphql-sync/?$", gql_http_sync_consumer),
            re_path("^graphql/?$", gql_http_async_consumer),
            re_path("^", django_asgi_app),  # This might be another endpoint in your app
        ]
    )
)
