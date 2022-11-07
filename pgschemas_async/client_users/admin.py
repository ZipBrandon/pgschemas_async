from django.contrib import admin
from django.contrib.admin import register

from client_users.models import ClientUser, ClientUserProfile


# Register your models here.


@register(ClientUser)
class ModelAdmin(admin.ModelAdmin):
    ...


@register(ClientUserProfile)
class ModelAdmin(admin.ModelAdmin):
    ...
