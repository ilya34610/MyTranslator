class TranslationHistoryModule:
    def __init__(self):
        print("Модуль истории переводов инициализирован.")
        self.history = []  # Список для хранения переводов

    def save_translation(self, source_text, translated_text, source_lang, target_lang, timestamp):
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
        print("Просмотр истории переводов:")
        if not self.history:
            print("История переводов пуста.")
        for record in self.history:
            print(f"Время: {record['timestamp']} | {record['source_lang']} -> {record['target_lang']}")
            print(f"Исходный текст: {record['source_text']}")
            print(f"Перевод: {record['translated_text']}\n")

    def search_history(self, query):
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
        print("Запуск модуля работы с историей переводов...")
        # Пример сохранения переводов
        self.save_translation("Привет", "Hello", "ru", "en", "2025-03-11 10:00")
        self.save_translation("Как дела?", "How are you?", "ru", "en", "2025-03-11 10:05")
        # Просмотр всей истории переводов
        self.view_history()
        # Поиск перевода по ключевому слову
        self.search_history("привет")
        print("Работа модуля истории переводов завершена.")


if __name__ == "__main__":
    history_module = TranslationHistoryModule()
    history_module.run()
