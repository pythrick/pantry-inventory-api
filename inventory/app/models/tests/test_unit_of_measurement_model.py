import uuid

import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestUnitOfMeasurementModel:
    def test_pk(self):
        obj = mixer.blend("inventory.app.UnitOfMeasurement")
        assert isinstance(
            obj.pk, uuid.UUID
        ), f"The {obj.__class__.__name__} pk should be an UUID field."

    def test_string(self):
        obj = mixer.blend("inventory.app.UnitOfMeasurement")
        assert str(obj) == f"{obj.name}"
