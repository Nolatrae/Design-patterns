import pytest
from src.models.nomenclature import Nomenclature

@pytest.fixture
def nomenclature():
    return Nomenclature()

@pytest.fixture
def other_nomenclature():
    return Nomenclature()

def test_initial_name(nomenclature):
    """Проверяет, что начальное значение имени пустое."""
    assert nomenclature.name == ""

def test_set_name(nomenclature):
    """Проверяет, что можно установить и получить имя."""
    nomenclature.name = "Test Name"
    assert nomenclature.name == "Test Name"

def test_local_equals_true(nomenclature, other_nomenclature):
    """Проверяет, что два объекта равны по имени."""
    nomenclature.name = "Same Name"
    other_nomenclature.name = "Same Name"
    assert nomenclature.local_equals(other_nomenclature) is True

def test_local_equals_false(nomenclature, other_nomenclature):
    """Проверяет, что два объекта не равны по имени."""
    nomenclature.name = "Name One"
    other_nomenclature.name = "Name Two"
    assert nomenclature.local_equals(other_nomenclature) is False
