from src.errors.base import MyTypeError, MyLengthError


class Valide:
    @staticmethod
    def validate(value, expected_type=None, expected_length=None):
        """
        Проверяет соответствие типа и длины переданного значения.

        :param value: проверяемое значение
        :param expected_type: ожидаемый тип данных (опционально)
        :param expected_length: ожидаемая длина значения (опционально)
        :raises InvalidTypeError: если тип значения не соответствует ожидаемому
        :raises InvalidLengthError: если длина значения не соответствует ожидаемой
        """

        # Проверка типа данных, если указан ожидаемый тип
        if expected_type and not isinstance(value, expected_type):
            raise MyTypeError(f"Значение должно быть типа {expected_type.__name__}, получен {type(value).__name__}")

        # Проверка длины, если указана ожидаемая длина и объект поддерживает len()
        if expected_length is not None:
            if not hasattr(value, '__len__'):
                raise MyLengthError("Объект не поддерживает вычисление длины")
            if len(value) != expected_length:
                raise MyLengthError(f"Длина должна быть {expected_length}, но получена {len(value)}")
