from django.contrib import admin

from inventory import models


class ItemInline(admin.TabularInline):
    model = models.ShoppingItem
    fields = ("product", "amount", "bought", "price")
    show_change_link = True


@admin.register(models.ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ("name", "purchase_date", "created_at")
    inlines = [ItemInline]
    search_fields = ("name",)
