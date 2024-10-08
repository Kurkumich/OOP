#--*-- encoding: cp1251 --*--
class Client:
    def __init__(self, client_id, last_name, first_name, middle_name, passport_number, passport_series):
        # Используем валидацию перед присвоением значений полям
        self.__client_id = Client.validate_client_id(client_id)
        self.__last_name = Client.validate_name(last_name)
        self.__first_name = Client.validate_name(first_name)
        self.__middle_name = Client.validate_name(middle_name)
        self.__passport_number = Client.validate_passport_number(passport_number)
        self.__passport_series = Client.validate_passport_series(passport_series)

    # Геттеры для получения значений полей
    def get_client_id(self):
        return self.__client_id

    def get_last_name(self):
        return self.__last_name

    def get_first_name(self):
        return self.__first_name

    def get_middle_name(self):
        return self.__middle_name

    def get_passport_number(self):
        return self.__passport_number

    def get_passport_series(self):
        return self.__passport_series

    # Сеттеры с валидацией
    def set_client_id(self, client_id):
        self.__client_id = Client.validate_client_id(client_id)

    def set_last_name(self, last_name):
        self.__last_name = Client.validate_name(last_name)

    def set_first_name(self, first_name):
        self.__first_name = Client.validate_name(first_name)

    def set_middle_name(self, middle_name):
        self.__middle_name = Client.validate_name(middle_name)

    def set_passport_number(self, passport_number):
        self.__passport_number = Client.validate_passport_number(passport_number)

    def set_passport_series(self, passport_series):
        self.__passport_series = Client.validate_passport_series(passport_series)

    # Метод для отображения информации о клиенте
    def display_client_info(self):
        print(f"Client ID: {self.__client_id}")
        print(f"Last Name: {self.__last_name}")
        print(f"First Name: {self.__first_name}")
        print(f"Middle Name: {self.__middle_name}")
        print(f"Passport Number: {self.__passport_number}")
        print(f"Passport Series: {self.__passport_series}")

    # Статические методы валидации

    @staticmethod
    def validate_client_id(client_id):
        if isinstance(client_id, int) and client_id > 0:
            return client_id
        else:
            raise ValueError("Client ID must be a positive integer.")

    @staticmethod
    def validate_name(name):
        if isinstance(name, str) and len(name.strip()) > 0:
            return name.strip()
        else:
            raise ValueError("Name fields must be non-empty strings.")

    @staticmethod
    def validate_passport_number(passport_number):
        if isinstance(passport_number, str) and passport_number.isdigit() and len(passport_number) == 6:
            return passport_number
        else:
            raise ValueError("Passport number must be a string of 6 digits.")

    @staticmethod
    def validate_passport_series(passport_series):
        if isinstance(passport_series, str) and len(passport_series) == 2 and passport_series.isalpha():
            return passport_series.upper()  # Преобразуем к верхнему регистру для единообразия
        else:
            raise ValueError("Passport series must be a string of 2 alphabetic characters.")
            

# Пример использования класса
if __name__ == "__main__":
    try:
        # Создаем объект с правильными значениями
        client = Client(1, "Ivanov", "Ivan", "Ivanovich", "123456", "AA")
        client.display_client_info()  # Выводим информацию о клиенте

        # Пытаемся создать объект с некорректным паспортным номером
        client_invalid = Client(2, "Petrov", "Petr", "Petrovich", "ABC123", "BB")
    except ValueError as e:
        print(f"Error: {e}")  # Обрабатываем ошибки валидации
