#--*-- encoding: cp1251 --*--
import json

class Client:
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], str):
                try:
                    if args[0].startswith('{') and args[0].endswith('}'):
                        self._from_json(args[0])
                    else:
                        self._from_string(args[0])
                except ValueError as e:
                    raise ValueError(f"Invalid string format: {e}")
            else:
                raise ValueError("Unsupported type for constructor. Expected string or JSON.")
        elif len(args) == 6:
            client_id, last_name, first_name, middle_name, passport_number, passport_series = args
            self.__client_id = Client.validate_client_id(client_id)
            self.__last_name = Client.validate_name(last_name)
            self.__first_name = Client.validate_name(first_name)
            self.__middle_name = Client.validate_name(middle_name)
            self.__passport_number = Client.validate_passport_number(passport_number)
            self.__passport_series = Client.validate_passport_series(passport_series)
        else:
            raise ValueError("Invalid constructor arguments.")

    def _from_string(self, client_str):
        parts = client_str.split(',')
        if len(parts) != 6:
            raise ValueError("String must contain exactly 6 comma-separated values.")
        client_id, last_name, first_name, middle_name, passport_number, passport_series = map(str.strip, parts)
        self.__client_id = Client.validate_client_id(int(client_id))
        self.__last_name = Client.validate_name(last_name)
        self.__first_name = Client.validate_name(first_name)
        self.__middle_name = Client.validate_name(middle_name)
        self.__passport_number = Client.validate_passport_number(passport_number)
        self.__passport_series = Client.validate_passport_series(passport_series)

    def _from_json(self, json_str):
        data = json.loads(json_str)
        required_keys = ["client_id", "last_name", "first_name", "middle_name", "passport_number", "passport_series"]
        if not all(key in data for key in required_keys):
            raise ValueError(f"JSON must contain all required fields: {required_keys}")
        self.__client_id = Client.validate_client_id(data["client_id"])
        self.__last_name = Client.validate_name(data["last_name"])
        self.__first_name = Client.validate_name(data["first_name"])
        self.__middle_name = Client.validate_name(data["middle_name"])
        self.__passport_number = Client.validate_passport_number(data["passport_number"])
        self.__passport_series = Client.validate_passport_series(data["passport_series"])

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

    def display_client_info(self):
        print(f"Client ID: {self.__client_id}")
        print(f"Last Name: {self.__last_name}")
        print(f"First Name: {self.__first_name}")
        print(f"Middle Name: {self.__middle_name}")
        print(f"Passport Number: {self.__passport_number}")
        print(f"Passport Series: {self.__passport_series}")

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
            return passport_series.upper()
        else:
            raise ValueError("Passport series must be a string of 2 alphabetic characters.")

if __name__ == "__main__":
    try:
        client_full = Client(1, "Ivanov", "Ivan", "Ivanovich", "123456", "AA")
        client_full.display_client_info()

        print("\n")

        client_from_str = Client("2, Petrov, Petr, Petrovich, 654321, BB")
        client_from_str.display_client_info()

        print("\n")

        json_data = '{"client_id": 3, "last_name": "Sidorov", "first_name": "Sidr", "middle_name": "Sidorovich", "passport_number": "987654", "passport_series": "CC"}'
        client_from_json = Client(json_data)
        client_from_json.display_client_info()

    except ValueError as e:
        print(f"Error: {e}")

