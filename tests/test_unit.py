from src.models.unit import Unit

def test_convert():
    base_unit = Unit("грамм", 1)
    new_unit = Unit("кг", 1000, base_unit)
    assert new_unit.to_base(2) == 2000
    assert new_unit.from_base(2000) == 2

