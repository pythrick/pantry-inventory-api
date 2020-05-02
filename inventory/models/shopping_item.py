from django.db import models
from django.utils.translation import gettext_lazy as _

from inventory.mixins import ModelMixin


class ShoppingItem(ModelMixin):
    class Meta:
        app_label = "inventory"
        db_table = "shopping_items"
        ordering = ("product__name",)
        verbose_name = _("Shopping Item")
        verbose_name_plural = _("Shopping Items")
        abstract = False

    product = models.ForeignKey(
        "Product", models.PROTECT, "shopping_items", "shopping_item"
    )
    shopping_list = models.ForeignKey(
        "ShoppingList", models.PROTECT, "shopping_items", "shopping_item"
    )
    amount = models.DecimalField(_("Amount"), max_digits=5, decimal_places=2)
    bought = models.NullBooleanField(
        _("Was bought?"), default=None, null=True, blank=True
    )
    price = models.DecimalField(
        _("Price"), max_digits=6, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return f"{self.shopping_list} - {self.product}"
