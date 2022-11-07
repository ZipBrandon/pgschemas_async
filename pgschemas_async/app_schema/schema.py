import strawberry
from strawberry_django_plus import gql

from app_schema import mutations, queries, subscriptions


@gql.type
class Queries(
    queries.Query,
):
    ...


@gql.type
class Mutations(
    mutations.Mutation,
):
    ...


@gql.type
class Subscriptions(
    subscriptions.Subscription,
):
    ...


schema = strawberry.Schema(
    query=Queries,
    mutation=Mutations,
    subscription=Subscriptions,
)
