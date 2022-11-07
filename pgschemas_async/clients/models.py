import uuid

from django.db import models
from django_pgschemas.models import DomainMixin, TenantMixin


class UUIDPrimaryKey(models.Model):
    """
    An abstract base class model that provides
    primary key id as uuid.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Client(
    UUIDPrimaryKey,
    TenantMixin,
):

    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]


class Domain(UUIDPrimaryKey, DomainMixin):
    def __str__(self):
        return f"{self.domain}"

    class Meta:
        ordering = ["tenant", "domain"]
