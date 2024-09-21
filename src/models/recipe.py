from src.interfaces.baseEntity import IEntity


class Recipe(IEntity):
    def __init__(self, name: str, ingredients: list, instructions: str):
        super().__init__()
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def local_eq(self, other: 'Recipe') -> bool:
        return (self.name, self.ingredients) == (other.name, other.ingredients)


class PersonalRecipe(Recipe):
    def __init__(self, name, ingredients, instructions):
        super().__init__(name, ingredients, instructions)

    def local_equals(self, other):
        return (
            isinstance(other, PersonalRecipe) and
            self.name == other.name and
            self.ingredients == other.ingredients
        )


class LessonRecipe(Recipe):
    def __init__(self, name: str, ingredients: list, instructions: str, lesson_topic: str):
        super().__init__(name, ingredients, instructions)
        self.lesson_topic = lesson_topic
