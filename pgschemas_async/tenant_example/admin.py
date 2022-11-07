from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin import register

from clients.models import Client, Domain
from tenant_example.models import TenantScopedModel


# Register your models here.


@register(TenantScopedModel)
class ModelAdmin(admin.ModelAdmin):
    ...
