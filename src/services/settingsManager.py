import json
import os
from src.models.settings import Settings


class SettingsManager:
    file_name = "settings.json"
    __settings = Settings()

    def __new__(cls):
        # Singleton pattern
        if not hasattr(cls, 'instance'):
            cls.instance = super(SettingsManager, cls).__new__(cls)
        return cls.instance

    @property
    def settings(self) -> Settings:
        return self.__settings

    def open_json(self, path: str = os.path.join(os.pardir, file_name)) -> None:
        if not isinstance(path, str):
            raise TypeError("File path should be a string")
        if not os.path.exists(path):
            raise FileNotFoundError(f"File {path} does not exist")

        with open(path, "r", encoding="utf-8") as f:
            file = json.load(f)
            for key, value in file.items():
                if hasattr(self.__settings, key):
                    try:
                        setattr(self.__settings, key, value)
                    except ValueError as e:
                        raise ValueError(f"Ошибка установки значения для {key}: {e}")

    def open_dict(self, input_dict: dict) -> None:
        """ Установка полей класса Settings из dict'а. """
        if not isinstance(input_dict, dict):
            raise TypeError("Var should be a dict")

        for key, value in input_dict.items():
            if hasattr(self.__settings, key):
                try:
                    setattr(self.settings, key, value)
                except ValueError as e:
                    print(f"Ошибка установки значения для {key}: {e}")
