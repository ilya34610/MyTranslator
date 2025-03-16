class TranslationHistoryModule:
    """
    Модуль управления историей переводов.

    Методы:
    - save_translation(source_text, translated_text, source_lang, target_lang, timestamp): Сохраняет перевод в историю.
    - view_history(): Отображает список сохранённых переводов.
    - search_history(query): Ищет переводы в истории по заданному запросу.
    - run(): Запускает процесс сохранения, просмотра и поиска переводов.
    """

    def __init__(self):
        """Инициализирует модуль истории переводов и создаёт список для хранения данных."""
        print("Модуль истории переводов инициализирован.")
        self.history = []

    def save_translation(self, source_text, translated_text, source_lang, target_lang, timestamp):
        """
        Сохраняет перевод в историю.

        :param source_text: Исходный текст.
        :param translated_text: Переведённый текст.
        :param source_lang: Язык исходного текста.
        :param target_lang: Язык перевода.
        :param timestamp: Временная метка перевода.
        """
        print("Сохранение перевода в историю...")
        record = {
            "source_text": source_text,
            "translated_text": translated_text,
            "source_lang": source_lang,
            "target_lang": target_lang,
            "timestamp": timestamp
        }
        self.history.append(record)
        print("Перевод успешно сохранен.")

    def view_history(self):
        """
        Отображает историю всех сохранённых переводов.
        """
        print("Просмотр истории переводов:")
        if not self.history:
            print("История переводов пуста.")
        for record in self.history:
            print(f"Время: {record['timestamp']} | {record['source_lang']} -> {record['target_lang']}")
            print(f"Исходный текст: {record['source_text']}")
            print(f"Перевод: {record['translated_text']}\n")

    def search_history(self, query):
        """
        Ищет переводы в истории по ключевому слову.

        :param query: Поисковый запрос.
        """
        print("Поиск по истории переводов...")
        results = []
        for record in self.history:
            if query.lower() in record['source_text'].lower() or query.lower() in record['translated_text'].lower():
                results.append(record)
        if results:
            print("Найденные переводы:")
            for record in results:
                print(f"Время: {record['timestamp']} | {record['source_lang']} -> {record['target_lang']}")
                print(f"Исходный текст: {record['source_text']}")
                print(f"Перевод: {record['translated_text']}\n")
        else:
            print("По заданному запросу переводы не найдены.")

    def run(self):
        """
        Запускает процесс управления историей переводов, включая сохранение, просмотр и поиск.
        """
        print("Запуск модуля работы с историей переводов...")
        self.save_translation("Привет", "Hello", "ru", "en", "2025-03-11 10:00")
        self.save_translation("Как дела?", "How are you?", "ru", "en", "2025-03-11 10:05")
        self.view_history()
        self.search_history("привет")
        print("Работа модуля истории переводов завершена.")


if __name__ == "__main__":
    """
    Точка входа в программу: создаёт экземпляр модуля и запускает его.
    """
    history_module = TranslationHistoryModule()
    history_module.run()
