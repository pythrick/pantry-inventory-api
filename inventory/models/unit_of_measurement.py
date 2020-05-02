from django.db import models
from django.utils.translation import gettext_lazy as _

from inventory.mixins import ModelMixin


class UnitOfMeasurement(ModelMixin):
    class Meta:
        app_label = "inventory"
        db_table = "units_of_measurement"
        ordering = ("name",)
        verbose_name = _("Unit of Measurement")
        verbose_name_plural = _("Units of Measurement")
        abstract = False

    name = models.CharField(_("Name"), max_length=100)

    def __str__(self):
        return self.name
