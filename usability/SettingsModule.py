class SettingsModule:
    """
    Модуль управления настройками.

    Методы:
    - load_settings(): Загружает сохранённые настройки.
    - update_setting(key, value): Обновляет указанную настройку.
    - save_settings(): Сохраняет текущие настройки.
    - reset_settings(): Сбрасывает настройки к значениям по умолчанию.
    - run(): Запускает процесс управления настройками.
    """

    def __init__(self):
        """Инициализирует модуль настроек и загружает сохранённые параметры."""
        print("Модуль настроек инициализирован.")
        self.settings = {
            "language": "ru",
            "theme": "light",
            "notifications": True
        }
        self.load_settings()

    def load_settings(self):
        """
        Загружает сохранённые настройки (псевдо-функция загрузки из файла или БД).
        """
        print("Загрузка сохраненных настроек...")
        print(f"Текущие настройки: {self.settings}")

    def update_setting(self, key, value):
        """
        Обновляет указанную настройку, если она существует.

        :param key: Название параметра.
        :param value: Новое значение параметра.
        """
        if key in self.settings:
            print(f"Изменение параметра {key}: {self.settings[key]} → {value}")
            self.settings[key] = value
        else:
            print(f"Ошибка: параметр {key} не найден.")

    def save_settings(self):
        """
        Сохраняет текущие настройки (псевдо-функция сохранения в файл или БД).
        """
        print("Сохранение настроек...")
        print(f"Настройки сохранены: {self.settings}")

    def reset_settings(self):
        """
        Сбрасывает настройки к значениям по умолчанию и сохраняет их.
        """
        print("Сброс настроек к значениям по умолчанию...")
        self.settings = {
            "language": "ru",
            "theme": "light",
            "notifications": True
        }
        self.save_settings()

    def run(self):
        """
        Запускает процесс управления настройками, вносит изменения и сохраняет их.
        """
        print("Запуск модуля управления настройками...")
        self.update_setting("theme", "dark")
        self.update_setting("language", "en")
        self.save_settings()
        print("Модуль настроек завершил работу.")


if __name__ == "__main__":
    """
    Точка входа в программу: создаёт экземпляр модуля и запускает его.
    """
    settings_module = SettingsModule()
    settings_module.run()
