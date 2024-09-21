from src.models.organization import Organization
from src.settingsManager import SettingsManager
import os


def test_create_instance():
    settings_manager = SettingsManager()
    path = os.path.join(os.pardir, "settings.json")
    settings_manager.from_json(path=path)
    settings = settings_manager.settings
    organization = Organization(settings)
    assert organization.inn == settings.inn
    assert organization.bik == settings.bik
    assert organization.account == settings.account
    assert organization.ownership_type == settings.ownership_type