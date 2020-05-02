from django.contrib import admin

from inventory import models


@admin.register(models.UnitOfMeasurement)
class UnitOfMeasurementAdmin(admin.ModelAdmin):
    list_display = ("name",)
