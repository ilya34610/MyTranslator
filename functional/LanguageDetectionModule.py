class LanguageDetectionModule:
    def __init__(self):
        print("Модуль автоматического определения языка инициализирован.")

    def preprocess_text(self, text):
        print("Предобработка текста: нормализация и удаление лишних символов...")
        # Псевдообработка: удаление пробелов и приведение к нижнему регистру
        processed_text = text.strip().lower()
        print(f"Предобработанный текст: {processed_text}")
        return processed_text

    def detect_language(self, text):
        print("Определение языка текста...")
        # Предобработка входного текста
        processed_text = self.preprocess_text(text)

        # Псевдоалгоритм определения языка на основе ключевых слов
        if "привет" in processed_text or "как дела" in processed_text:
            language = "ru"
        elif "hello" in processed_text or "how are you" in processed_text:
            language = "en"
        else:
            language = "undetermined"

        print(f"Определённый язык: {language}")
        return language

    def run(self, text):
        print("Запуск модуля автоматического определения языка...")
        language = self.detect_language(text)
        print("Определение языка завершено.")
        return language


if __name__ == "__main__":
    lang_detection = LanguageDetectionModule()
    sample_text = "Привет, как дела?"
    detected_language = lang_detection.run(sample_text)
