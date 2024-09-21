import pytest
from src.baseRepo import BaseRepo
from src.models.nomenclature import Nomenclature
from src.models.unit import Unit
from src.models.nomenclatureGroup import GroupNomenclature
from src.models.recipe import PersonalRecipe


@pytest.fixture
def repository():
    """Фикстура для создания репозитория данных перед каждым тестом."""
    return BaseRepo()


def test_nomenclature(repository):
    """Тест для проверки добавления и корректного хранения номенклатуры."""
    nomenclature = Nomenclature()
    nomenclature.name = "Товар A"
    repository.storage["nomenclature"] = nomenclature

    assert "nomenclature" in repository.storage, "Номенклатура должна присутствовать в хранилище"
    assert isinstance(repository.storage["nomenclature"], Nomenclature), "Должен быть экземпляр Nomenclature"
    assert repository.storage["nomenclature"].name == "Товар A", "Название номенклатуры должно совпадать с ожидаемым"


def test_units_of_measurement(repository):
    """Тест для проверки добавления и хранения единиц измерения."""
    kilogram = Unit(name="Килограмм", conversion_factor=1.0)
    gram = Unit(name="Грамм", conversion_factor=0.001, base_unit=kilogram)

    repository.storage["units"] = {"kilogram": kilogram, "gram": gram}

    assert "units" in repository.storage, "Единицы измерения должны присутствовать в хранилище"
    assert "kilogram" in repository.storage["units"], "Килограмм должен присутствовать в единицах измерения"
    assert isinstance(repository.storage["units"]["kilogram"], Unit), "Должен быть экземпляр Unit"
    assert repository.storage["units"]["kilogram"].name == "Килограмм", "Название должно быть 'Килограмм'"
    assert repository.storage["units"]["gram"].conversion_factor == 0.001, "Неверный коэффициент конверсии для грамма"


def test_groups(repository):
    """Тест для проверки добавления и хранения групп номенклатуры."""
    group = GroupNomenclature.create_base_group()
    repository.storage["group"] = group

    assert "group" in repository.storage, "Группа должна присутствовать в хранилище"
    assert isinstance(repository.storage["group"], GroupNomenclature), "Тип группы должен быть GroupNomenclature"


def test_recipes(repository):
    """Тест для проверки добавления и получения рецептов."""
    recipe = PersonalRecipe(name="Запеканка", ingredients=["Тесто", "Помидор"], instructions="Готовить 2 часа.")
    repository.save_recipe(recipe)

    recipes = repository.fetch_recipes()

    assert len(recipes) > 0, "Должен быть хотя бы один рецепт в репозитории"
    assert recipes[0].name == "Запеканка", "Название рецепта должно быть 'Запеканка'"
    assert "Тесто" in recipes[0].ingredients, "Ингредиенты должны включать 'Тесто'"
