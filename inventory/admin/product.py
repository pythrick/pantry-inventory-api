from django.contrib import admin

from inventory import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "unit_of_measurement")
