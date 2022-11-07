from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from clients.models import Client, Domain

        client1, created = Client.objects.get_or_create(
            schema_name="client1", name="Client 1"
        )
        Domain.objects.get_or_create(
            domain="client1.zd-local.com", tenant=client1, is_primary=True
        )

        client2, created_2 = Client.objects.get_or_create(
            schema_name="client2", name="Client 2"
        )
        Domain.objects.get_or_create(
            domain="client2.zd-local.com", tenant=client2, is_primary=True
        )
