class Unit:
    def __init__(self, name: str, conversion_factor: float, base_unit=None):
        """
        Инициализация единицы измерения.

        :param name: Название единицы измерения.
        :param conversion_factor: Коэффициент пересчета в базовую единицу.
        :param base_unit: Базовая единица измерения, в которой осуществляется пересчет. Если не указана, используется сама единица.
        """
        self.name = name
        self.conversion_factor = conversion_factor
        self.base_unit = base_unit if base_unit else self

    def to_base(self, value: float) -> float:
        """
        Переводит значение в базовые единицы.

        :param value: Значение в текущих единицах.
        :return: Значение в базовых единицах.
        """
        return value * self.conversion_factor

    def from_base(self, value: float) -> float:
        """
        Переводит значение из базовых единиц в текущие единицы.

        :param value: Значение в базовых единицах.
        :return: Значение в текущих единицах.
        """
        return value / self.conversion_factor

    def __str__(self) -> str:
        """
        Возвращает строковое представление единицы измерения.

        :return: Строковое представление единицы измерения.
        """
        base_unit_info = f", базовая единица: {self.base_unit.name}" if self.base_unit != self else ""
        return f"{self.name} (коэффициент пересчета: {self.conversion_factor}{base_unit_info})"
