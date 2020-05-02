from django.db import models
from django.utils.translation import gettext_lazy as _

from inventory.mixins import ModelMixin


class Item(ModelMixin):
    class Meta:
        app_label = "inventory"
        db_table = "items"
        ordering = ("product__name",)
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
        abstract = False

    product = models.ForeignKey("Product", models.PROTECT, "items", "item")
    amount = models.DecimalField(_("Amount"), max_digits=5, decimal_places=2)
    expiration_date = models.DateField(_("Expiration date"), null=True, blank=True)

    def __str__(self):
        return f"{self.product}: {self.amount} {self.product.unit_of_measurement.name}"
