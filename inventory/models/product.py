from django.db import models
from django.utils.translation import gettext_lazy as _

from inventory.mixins import ModelMixin


class Product(ModelMixin):
    class Meta:
        app_label = "inventory"
        db_table = "products"
        ordering = ("name",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        abstract = False

    name = models.CharField(_("Name"), max_length=100)
    description = models.TextField(_("Description"))
    unit_of_measurement = models.ForeignKey(
        "UnitOfMeasurement", models.PROTECT, "products", "product"
    )

    def __str__(self):
        return self.name
