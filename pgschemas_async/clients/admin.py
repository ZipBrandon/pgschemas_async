from django.contrib import admin
from django.contrib.admin import register

from clients.models import Client, Domain


# Register your models here.


@register(Client)
class ModelAdmin(admin.ModelAdmin):
    ...


@register(Domain)
class ModelAdmin(admin.ModelAdmin):
    ...
