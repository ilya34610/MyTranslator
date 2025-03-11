class DataSecurityModule:
    def __init__(self):
        print("Модуль безопасности данных инициализирован.")

    def encrypt_data(self, plaintext):
        print("Шифрование данных...")
        # Пример простого шифрования: реверс строки
        encrypted = plaintext[::-1]
        print(f"Данные зашифрованы: {encrypted}")
        return encrypted

    def decrypt_data(self, encrypted):
        print("Дешифрование данных...")
        # Восстановление исходного текста путем реверса строки
        decrypted = encrypted[::-1]
        print(f"Данные расшифрованы: {decrypted}")
        return decrypted

    def secure_storage(self, data):
        print("Сохранение данных в защищенное хранилище...")
        encrypted_data = self.encrypt_data(data)
        print("Данные успешно сохранены в защищенном виде.")
        return encrypted_data

    def retrieve_data(self, encrypted_data):
        print("Извлечение данных из защищенного хранилища...")
        decrypted_data = self.decrypt_data(encrypted_data)
        print("Данные успешно извлечены и расшифрованы.")
        return decrypted_data


if __name__ == "__main__":
    security_module = DataSecurityModule()
    sample_data = "Конфиденциальные данные пользователя"

    # Сохранение данных
    stored_data = security_module.secure_storage(sample_data)

    # Извлечение данных
    retrieved_data = security_module.retrieve_data(stored_data)
