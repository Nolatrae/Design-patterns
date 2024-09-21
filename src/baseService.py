from src.errors.valide import Valide
from src.models.recipe import LessonRecipe, PersonalRecipe
from src.settingsManager import SettingsManager
from src.baseRepo import BaseRepo
from src.models.nomenclatureGroup import GroupNomenclature
from src.models.nomenclature import Nomenclature
from src.models.unit import Unit


class RecipeService:
    __repository: BaseRepo = None
    __settings_manager: SettingsManager = None

    def __init__(self, repository: BaseRepo, settings_manager: SettingsManager):
        Valide.validate(repository, BaseRepo)
        Valide.validate(settings_manager, SettingsManager)
        self.__repository = repository
        self.__settings_manager = settings_manager

    @property
    def settings(self):
        return self.__settings_manager.settings

    def create_personal_recipe(self):
        """Создаёт и сохраняет личный рецепт."""
        personal_recipe = PersonalRecipe(
            name="Личный рецепт",
            ingredients=["Ингредиент 1", "Ингредиент 2"],
            instructions="Инструкции для личного рецепта"
        )
        self.__repository.save_recipe(personal_recipe)

    def create_lesson_recipe(self):
        """Создаёт и сохраняет рецепт для занятия."""
        lesson_recipe = LessonRecipe(
            name="Рецепт для занятия",
            ingredients=["Ингредиент A", "Ингредиент B"],
            instructions="Инструкции для рецепта занятия",
            lesson_topic="Тема занятия"
        )
        self.__repository.save_recipe(lesson_recipe)

    def create_nomenclature(self):
        """Создаёт и сохраняет номенклатуру."""
        nomenclature = Nomenclature()
        nomenclature.name = "Товар A"
        self.__repository.storage["nomenclature"] = nomenclature

    def create_group(self):
        """Создаёт и сохраняет группу."""
        base_group = GroupNomenclature.create_base_group()
        self.__repository.storage["group"] = base_group

    def create_units(self):
        """Создаёт и сохраняет единицы измерения."""
        kilogram = Unit(name="Килограмм", conversion_factor=1.0)
        gram = Unit(name="Грамм", conversion_factor=0.001, base_unit=kilogram)
        self.__repository.storage["units"] = {"kilogram": kilogram, "gram": gram}

    def create(self):
        """Основной метод для создания данных: рецепты, номенклатура, группы и единицы измерения."""
        self.create_personal_recipe()
        self.create_lesson_recipe()
        self.create_nomenclature()
        self.create_group()
        self.create_units()

        print("Рецепты, номенклатура, группы и единицы измерения успешно созданы.")
