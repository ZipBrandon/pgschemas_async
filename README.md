## Installation

1. Clone the project
2. cd into `pgschemas_async`
3. `docker compose up`
4. Migrations will be run and data will be bootstrapped which creates `client1` and `client2`.
5. Navigate to `http://client1.zd-local.com:10000/graphql` ( Note: *.zd-local.com's DNS will resolve to 127.0.0.1 )
6. Execute the example graphql for `getClient` and `getClientSync`


## Async Resolver loses `get_current_schema`

`getClient` is async and `getClientSync` is sync.

The return of the `currentSchema` should reflect the current schema that was activated from `MyTenantProtocolRouter` in its overridden `__call__`. My expectations are that all database queries would fall under the activated client1's schema, but it will only do this in sync resolution. Am I missing a concept?


Executing the example query
```graphql
{
  getClient {
    id
    name
    currentSchema
  }
  getClientSync {
    id
    name
    currentSchema
  }
}
```

Results in:
```json
{
  "data": {
    "getClient": {
      "id": "990a30fd-7495-414a-b2b0-c377b132aecd",
      "name": "Client 1",
      "currentSchema": "public"
    },
    "getClientSync": {
      "id": "990a30fd-7495-414a-b2b0-c377b132aecd",
      "name": "Client 1",
      "currentSchema": "client1"
    }
  }
}
```

The reflection of the `id` and `name` of the client are only retrieved from the context value that I provided to it in `MyDjangoChannelsContext`