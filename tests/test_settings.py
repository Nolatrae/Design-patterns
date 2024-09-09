import pytest
from src.models.settings import Settings
from src.services.settings import SettingsManager


def test_inn_valid():
    settings = Settings()
    settings.inn = "123456789012"
    assert settings.inn == "123456789012"


def test_inn_invalid():
    settings = Settings()
    with pytest.raises(ValueError, match="ИНН должен быть строкой и содержать 12 символов."):
        settings.inn = "123456"


def test_account_valid():
    settings = Settings()
    settings.account = "12345678901"
    assert settings.account == "12345678901"


def test_account_invalid():
    settings = Settings()
    with pytest.raises(ValueError, match="Счет должен быть строкой и содержать 11 символов."):
        settings.account = "12345"


def test_corr_account_valid():
    settings = Settings()
    settings.corr_account = "12345678901"
    assert settings.corr_account == "12345678901"


def test_corr_account_invalid():
    settings = Settings()
    with pytest.raises(ValueError, match="Корреспондентский счет должен быть строкой и содержать 11 символов."):
        settings.corr_account = "12345"


def test_bik_valid():
    settings = Settings()
    settings.bik = "123456789"
    assert settings.bik == "123456789"


def test_bik_invalid():
    settings = Settings()
    with pytest.raises(ValueError, match="БИК должен быть строкой и содержать 9 символов."):
        settings.bik = "12345"


def test_name_valid():
    settings = Settings()
    settings.name = "Test Name"
    assert settings.name == "Test Name"


def test_name_invalid():
    settings = Settings()
    with pytest.raises(ValueError, match="Наименование должно быть строкой."):
        settings.name = 12345


def test_ownership_type_valid():
    settings = Settings()
    settings.ownership_type = "ABCDE"
    assert settings.ownership_type == "ABCDE"


def test_ownership_type_invalid():
    settings = Settings()
    with pytest.raises(ValueError, match="Вид собственности должен быть строкой и содержать 5 символов."):
        settings.ownership_type = "ABC"


def test_singleton_settings_manager():
    instance1 = SettingsManager()
    instance2 = SettingsManager()

    assert instance1 is instance2
