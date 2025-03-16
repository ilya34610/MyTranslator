class DataSecurityModule:
    """
    Модуль безопасности данных.

    Методы:
    - encrypt_data(plaintext): Шифрует переданные данные (реверс строки в данном примере).
    - decrypt_data(encrypted): Дешифрует переданные данные (обратный реверс строки).
    - secure_storage(data): Сохраняет данные в защищенном виде.
    - retrieve_data(encrypted_data): Извлекает и расшифровывает данные из хранилища.
    """

    def __init__(self):
        """Инициализирует модуль безопасности данных."""
        print("Модуль безопасности данных инициализирован.")

    def encrypt_data(self, plaintext):
        """
        Шифрует данные с помощью реверса строки (простой метод шифрования).

        :param plaintext: Исходные данные.
        :return: Зашифрованные данные.
        """
        print("Шифрование данных...")
        encrypted = plaintext[::-1]
        print(f"Данные зашифрованы: {encrypted}")
        return encrypted

    def decrypt_data(self, encrypted):
        """
        Дешифрует данные, восстанавливая исходную строку.

        :param encrypted: Зашифрованные данные.
        :return: Расшифрованные данные.
        """
        print("Дешифрование данных...")
        decrypted = encrypted[::-1]
        print(f"Данные расшифрованы: {decrypted}")
        return decrypted

    def secure_storage(self, data):
        """
        Сохраняет данные в зашифрованном виде.

        :param data: Исходные данные.
        :return: Зашифрованные данные, сохраненные в хранилище.
        """
        print("Сохранение данных в защищенное хранилище...")
        encrypted_data = self.encrypt_data(data)
        print("Данные успешно сохранены в защищенном виде.")
        return encrypted_data

    def retrieve_data(self, encrypted_data):
        """
        Извлекает и расшифровывает данные из защищенного хранилища.

        :param encrypted_data: Зашифрованные данные.
        :return: Расшифрованные данные.
        """
        print("Извлечение данных из защищенного хранилища...")
        decrypted_data = self.decrypt_data(encrypted_data)
        print("Данные успешно извлечены и расшифрованы.")
        return decrypted_data


if __name__ == "__main__":
    """
    Точка входа в программу: создаёт экземпляр модуля и тестирует его на конфиденциальных данных.
    """
    security_module = DataSecurityModule()
    sample_data = "Конфиденциальные данные пользователя"

    stored_data = security_module.secure_storage(sample_data)
    retrieved_data = security_module.retrieve_data(stored_data)
