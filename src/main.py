from src.services.settings import SettingsManager
import os


if __name__ == "__main__":
    settingsManager = SettingsManager()
    settingsManager.open_json(os.path.join(os.pardir, "settings.json"))

    settings = settingsManager.settings
    print(settings)


