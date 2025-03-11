class TextIOBlock:
    def __init__(self):
        print("Модуль ввода и вывода текста инициализирован.")

    def input_text(self):
        print("Выберите способ ввода текста:")
        print("1. Ввод с клавиатуры")
        print("2. Загрузка текста из файла")
        choice = input("Введите номер метода ввода: ")

        if choice == "1":
            text = input("Введите текст: ")
        elif choice == "2":
            filepath = input("Введите путь к файлу: ")
            text = self.read_file(filepath)
        else:
            print("Некорректный выбор. Повторите ввод.")
            text = self.input_text()  # Рекурсивный вызов для повторного ввода
        return text

    def read_file(self, filepath):
        print(f"Чтение файла: {filepath}")
        # Псевдореализация: в реальной реализации здесь осуществляется поддержка форматов TXT, DOCX, PDF.
        text = "Содержимое файла (симуляция)"
        return text

    def output_text(self, text):
        print("Выберите способ вывода текста:")
        print("1. Вывод на экран")
        print("2. Сохранение текста в файл")
        choice = input("Введите номер метода вывода: ")

        if choice == "1":
            print("Результат:")
            print(text)
        elif choice == "2":
            filepath = input("Введите путь для сохранения файла: ")
            self.write_file(filepath, text)
        else:
            print("Некорректный выбор. Повторите ввод.")
            self.output_text(text)  # Рекурсивный вызов для повторного ввода

    def write_file(self, filepath, text):
        print(f"Сохранение текста в файл: {filepath}")
        # Псевдореализация: здесь производится запись текста в файл
        print("Текст успешно сохранён.")

    def run(self):
        print("Запуск функционального блока ввода и вывода текста...")
        user_text = self.input_text()
        # Здесь можно интегрировать обработку текста, перевод и т.п.
        self.output_text(user_text)
        print("Работа с вводом и выводом текста завершена.")


if __name__ == "__main__":
    io_block = TextIOBlock()
    io_block.run()
