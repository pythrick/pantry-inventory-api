from django.db import models
from django.utils.translation import gettext_lazy as _

from inventory.mixins import ModelMixin


class ShoppingList(ModelMixin):
    class Meta:
        app_label = "inventory"
        db_table = "shopping_list"
        ordering = ("created_at",)
        verbose_name = _("Shopping List")
        verbose_name_plural = _("Shopping Lists")
        abstract = False

    name = models.CharField(_("Name"), max_length=100)
    products = models.ManyToManyField(
        "Product", "shopping_lists", "shopping_list", through="ShoppingItem"
    )
    purchase_date = models.DateField(_("Purchase date"), null=True, blank=True)

    def __str__(self):
        return self.name
