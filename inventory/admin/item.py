from django.contrib import admin

from inventory import models


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("product", "amount", "expiration_date")
