class BaseRepo:
    __storage = {}
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(BaseRepo, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    @staticmethod
    def recipe_key():
        return "recipes"

    @staticmethod
    def category_key():
        return "categories"

    @staticmethod
    def unit_key():
        return "units"

    @property
    def storage(self):
        return self.__storage

    def add_item(self, key, item):
        """
        Универсальный метод для добавления элемента в хранилище по ключу.
        Если ключа не существует, создаётся новый список.
        """
        if key not in self.__storage:
            self.__storage[key] = []
        self.__storage[key].append(item)

    def get_items(self, key):
        """
        Универсальный метод для получения элементов по ключу.
        Возвращает пустой список, если ключ не найден.
        """
        return self.__storage.get(key, [])

    def save_recipe(self, recipe):
        """Метод для добавления рецепта в хранилище."""
        self.add_item(self.recipe_key(), recipe)

    def fetch_recipes(self):
        """Метод для получения всех рецептов."""
        return self.get_items(self.recipe_key())

    def add_category(self, category):
        """Метод для добавления категории."""
        self.add_item(self.category_key(), category)

    def get_categories(self):
        """Метод для получения всех категорий."""
        return self.get_items(self.category_key())

    def add_unit(self, unit):
        """Метод для добавления единицы измерения."""
        self.add_item(self.unit_key(), unit)

    def get_units(self):
        """Метод для получения всех единиц измерения."""
        return self.get_items(self.unit_key())
