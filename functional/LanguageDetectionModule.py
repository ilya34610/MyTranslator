class LanguageDetectionModule:
    """
    Модуль автоматического определения языка.

    Методы:
    - preprocess_text(text): Предобрабатывает текст перед анализом.
    - detect_language(text): Определяет язык текста на основе ключевых слов.
    - run(text): Запускает процесс определения языка.
    """

    def __init__(self):
        """Инициализирует модуль автоматического определения языка."""
        print("Модуль автоматического определения языка инициализирован.")

    def preprocess_text(self, text):
        """
        Предобрабатывает текст: нормализует и удаляет лишние символы.

        :param text: Исходный текст.
        :return: Предобработанный текст.
        """
        print("Предобработка текста: нормализация и удаление лишних символов...")
        processed_text = text.strip().lower()
        print(f"Предобработанный текст: {processed_text}")
        return processed_text

    def detect_language(self, text):
        """
        Определяет язык текста на основе ключевых слов.

        :param text: Исходный текст.
        :return: Код языка (например, 'ru' для русского, 'en' для английского, 'undetermined' если язык не распознан).
        """
        print("Определение языка текста...")
        processed_text = self.preprocess_text(text)

        if "привет" in processed_text or "как дела" in processed_text:
            language = "ru"
        elif "hello" in processed_text or "how are you" in processed_text:
            language = "en"
        else:
            language = "undetermined"

        print(f"Определённый язык: {language}")
        return language

    def run(self, text):
        """
        Запускает процесс автоматического определения языка.

        :param text: Исходный текст.
        :return: Определённый код языка.
        """
        print("Запуск модуля автоматического определения языка...")
        language = self.detect_language(text)
        print("Определение языка завершено.")
        return language


if __name__ == "__main__":
    """
    Точка входа в программу: создаёт экземпляр модуля и запускает его на тестовом тексте.
    """
    lang_detection = LanguageDetectionModule()
    sample_text = "Привет, как дела?"
    detected_language = lang_detection.run(sample_text)
